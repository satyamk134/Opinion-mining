# -*- coding: utf-8 -*-
from __future__ import division

import nltk
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from collections import Counter
from nltk.corpus import stopwords
from external.my_potts_tokenizer import MyPottsTokenizer

from external.my_potts_tokenizer import MyPottsTokenizer
import pandas as pd
import numpy as np
from score_aspect import *


def get_sentences(review):
    """
    INPUT: full text of a review
    OUTPUT: a list of sentences
    Given the text of a review, return a list of sentences.
    """

    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

    if isinstance(review, str):
        return sent_detector.tokenize(review)
    else:
        raise TypeError('Sentence tokenizer got type %s, expected string' % type(review))

def tokenize(sentence):
	"""
	INPUT: string (full sentence)
	OUTPUT: list of strings
	Given a sentence in string form, return
	a tokenized list of lowercased words.
	"""

	pt = MyPottsTokenizer(preserve_case=False)
	return pt.tokenize(sentence)

def pos_tag(toked_sentence):
	"""
	INPUT: list of strings
	OUTPUT: list of tuples
	Given a tokenized sentence, return
	a list of tuples of form (token, POS)
	where POS is the part of speech of token
	"""
	return nltk.pos_tag(toked_sentence)

def aspects_from_tagged_sents(tagged_sentences):
	"""
	INPUT: list of lists of strings
	OUTPUT: list of aspects
	Given a list of tokenized and pos_tagged sentences from reviews
	about a given restaurant, return the most common aspects
	"""

	STOPWORDS = set(stopwords.words('english'))

	# find the most common nouns in the sentences
	noun_counter = Counter()

	for sent in tagged_sentences:
		for word, pos in sent:
			if pos=='NNP' or pos=='NN' and word not in STOPWORDS:
				noun_counter[word] += 1

	# list of tuples of form (noun, count)
	return [noun for noun, _ in noun_counter.most_common(10)]


def score_aspect(reviews, aspect):
    """
    INPUT: iterable of reviews, iterable of aspects
    OUTPUT: score of aspect on given set of reviews

    For a set of reviews and corresponding aspects,
    return the score of the aspect on the reviews
    """


    from score_aspect import SentimentScorer, get_sentences_by_aspect

    sentiment_scorer = SentimentScorer()
    aspect_sentences = get_sentences_by_aspect(aspect, reviews)
    scores = [sentiment_scorer.score(sent) for sent in aspect_sentences]
    #print scores
    print aspect_sentences
    #print np.mean(scores)
    return 1#np.mean(scores)

def aspect_opinions(reviews):
	"""
	INPUT: a set of reviews
	OUTPUT: dictionary with aspects as keys and values as scores
	"""

	aspects = [u'food', u'place', u'service', u'ambience', u'restaurant', u'staff', u'experience', u'dinner', u'breakfast', u'time']
	return dict([(aspect, score_aspect(reviews, aspect)) for aspect in aspects])




if __name__ == "__main__":
    reviews = """Description of the place: The place is dim lit at night & adds to a tranquil & romantic ambience.Food: The only issue I have is that some of their dishes are a little bland & the desserts tasted eggy.Recommendation: I loved their jasmine rice, wontons & baos. 
 Mixing different Asian cuisines can be a tricky task. The Fatty Bao however does a great job of doing justice to all the different cuisines it offers. My friends and I couldn’t stop eating as we kept trying different dishes ( none of it disappointing). The service and ambience were great too. 
 This place is Bangalore's first ever Asian Gastro Pub with innovative food and amazing ambience. The place has some classy decor and amazing tables.
 One of my favorite hangouts in this part of town. Not only are the baos nice, the other stuff in their menu is good as well. The terrace sitting arrangement is a temptation that is hard to resist.
The place serves a huge variety of menu. To specify I quite like the sushi here, unlike many places the blend and the preparation here is just perfect. The Roasted Duck Lamb were good and so was the Crispy Cauliflower with Garlic, celery & coriander. I quite liked their Lamb with young peppercorns & Thai herbs which had its rich Asian flavors as expected. I was quite full and did not order any desserts even though it was hard to resist after viewing their menu. 
 This restaurant is located just near suksagar koramangla 5th block, Visited this place yesterday, it look's very attractive from outside, good place for family, we had directly main course didn't go for starters, because we didn't had much time, but service was excellent,as well as the ambience, we'll visit again for sure..
 You can expect superb food here. My wife and I were here for our anniversary lunch and the food just made our day even better. Wanton soup, dimsum platter and Thai green curry were all fantastic. Banana rolls for dessert was refreshing with really high quality ice cream. Staff were courteous and never in hurry to serve. Speed of service was just right too. Must visit if you love Thai food. 
We tried out the sushi, both the veg and non veg sushi was really good. I love sushi to I decided to skip lunch and just stick to this. The cocktail were good. everyone liked the whisky sour.
The food looked beautiful but things were off. The crystal dumplings has sticky undercooked batter and oily residue. the spicy salmon roll did not have uniform pieces and poor wrapping. the avocado vegetable sushi was nice. the tempura mixed veg fritters were too large and oily though a nice "pakoda" like dish. 
 Really a nice place with live music if you are lucky.
 I honestly had a fabulous first experience here! The food was cooked to perfection, but then when I speak about my great reviews to others, thy disagree. Maybe it was beginners luck
After doing analysis for an hour, we finally made up our mind for this place. They had extensive options out of which we ordered Blueberry Tango, Lemonade, spring rolls, kimchi sushi, Yakisoba egg noodles, mushroom cream dumplings, cocobar and cheese cake. Taste wise everything tasted heavenly delicious and it couldn't have been better than what it was.
Had a couple of cocktails in mandarini and Chinese spring cup. The cocktails were really amazing with decent mix of flavours and white rum. Spring cup was with cranberry flavor and mandarini was a mix of sweet and bitter flavour with white rum.
beautiful place and lovely people. this place is all I want on a lazy Sunday with a wholesome pasta and hukka.... staff is polite and always smiling and happy to help as if they are never tired of working in the place. In the evening the dj takes over and plays cool Punjabi songs... love the place and people and food although hukka can be a bit better...... 
This place is an absolute pleasure to be in. Calm, breezy, quite and the house playing some good dance tunes. I tried the veg food there and it was really good. Especially the deep fried corn starter and money bag. I'm giving 4 stars because they didn't have a complete menu yet. Surely looking forward to going back here once they have a complete menu. 
 This newly opened restaurant is worth trying. The ambience is similar to Float restaurant, the decor infused with blue, white and pale green curtains and cushions. The ambience is really pleasing to the eye. 
Ambience - Was here for dinner on a Saturday night and I loved the way the place was lit up! Despite being a weekend night the place was not crowded.  You get a feeling of being transported to a new place! They have a very comfortable seating with wooden dining tables with cushioned chairs. The main highlight of the place is the open kitchen which right at the center of the restaurant. There was big screen on the right corner of the restaurant in which a sports channel was playing. Decor is very simple with Asian themed sketches on the wall. Everything put together you get a very soothing vibe here! 
The Staff is very good. They are polite, attentive and always on their toes to serve their customers. The service was pretty quick. We asked for the soup first and then the drinks along with the starter and they promptly came and asked us if we are ready for our drinks once we were done with our Soup! They customized a dish for us and also prepared a starter which was not on the menu. 
Broccoli and cheese baos: As light as could be, extremely fluffy and tasted amazing.
Great food and very good service. Now it’s usually very crowded. Closes early too but the food is great!
Had heard a lot about this place. Finally went there with friends. Love the decor and the ambience. We got a place on the first floor along the balcony. But it took a lot of effort to get the staff's attention.
This is one place which had 5 stars on several review sites. Finally I landed at the place on one Sunday morning only to wait for an hour to get my seat.
Had the English breakfast here. The way they fry the bacon out here is the best. I loved the peanut and banana smoothie and the chocolate waffles too. Must try!
what a full breakfast - well done eggs, bacon, sausages, ham, hash brown et all. Its okay to cheat on the calories (and its a lot of it) once in a while for the amazing stuff.
 I ordered the porky fellas breakfast which was really good the chorizo sausage was insane and so were the accompaniments
I visited hole in wall cafe with my son.Breakfast was tasty,delicious and very healthy.Ambience was excellent.I enjoyed a lot.
I recently visited hole in the wall cafe with my friends. Really enjoyed there. It was the best breakfast ever.
This cafe has perfected the art of giving soft buns, juicy meat and yummy desserts. They have a decent vegetarian menu option, my favourite has been the spinach omelette.
Lively atmosphere, amazing crowd and staff and quality food is how I would summarise this place. The All English breakfast, banana waffle and paneer burger is a must try.
The Ambience is very innovative and refreshing. Preparation is also very nice...But huge waiting was there so plan accordingly.
This upper end cafe in the posh Area attracts most people for a lovely relaxed and satisfying feeling in being in a nice cafe 
So this is a nice eatery on 100 feet road . Definitely recommend their pancakes and chicken pasta 
Im here all the time just for the "All Day Breakfast" and I totally love the food here. The waffles here is a must try here.
The food is just fantastic! The ambience is fabulous. Do look out for their Hangover menu, it does work :p Try out the desserts and the pancakes they are just finger licking good!
Did a breakfast on a hungry morning.. Good waffles..well done cheese omlettes.. And a good masala chai.sure made me a happy soul
This place was amazing! The food was sooo tasty and the staff was very nice and friendly. We ordered a couple of things to share for a group. We especially enjoyed the spring rolls and soup dumplings.
I am no expert in dim sum. But this was absolutely delicious. The ambiance of the restaraunt was unique and the wait staff was excellent.
Every time I've eaten here, the food has been exquisite 
One of the best authentic Oriental food that I have had in recent times. And the staff is extremely courteous.
It was a little challenging to find the restaurant, but once asked, we were led down elevators through wine shelves to find a very nice dinning area.
The one with Shrimp stood out for me.The mains were delicious too.
Yes please. They make their dumplings in house and the service was exceptional. Sitting outside with a drink was the perfect way to end a day.
The dim sum was not only delicious but the presentation was up there with the best I have had in Hong Kong, New York, Toronto and across China. Some of my choices were the lobster dumplings, spinach and mushroom dumplings, chow foon wrapped shrimp, and clay pot chicken. All excellent. I was so impressed I inquired on the chef expecting to hear that he/she was from Hong Kong but in fact the chef was from Malaysia.
I was late for my reservation, yet no problem. I also asked for something they only had in another on-prem restaurant and they sent someone for it. Nice.
Very good service and great food. The staff is attentive to your every need and very warm. Food was always delicious.
Amazing ambience! We were given a private room for candlelight dinner with all are old photographs stuck as a surprise. The food was absolutely wonderful, from preparation to presentation, very pleasing. 
Truly impressive experience while at lunch with colleagues. Great food quality, attentive team & overall a impressive experience
Had a lovely dinner the last time and went again the next time. Good dim sums and great soup.Courteous staff, and good atmosphere.wKK LOVE TO GO BACK.
Excellent place to spend for a lovely lunch with friends and family.
Wait staff were excellent as was the menu. There is something on the menu for everyone. The food is very tasty and the portions are more than enough. I can highly recommend this restaurant.
went on a dinner date.. they made it perfect .. its a beautiful place to hop in with your loved ones .. lovely ambience with peaceful music. food would mesmerise your taste buds .
Cabana seat i like very much. Nice view on the night. Very beautiful!!
Amazing dining experience. Calm and private dining, and the food is simply amazing. The chef himself came to greet us. Honestly the best in Bangalore, highly recommended.
I had dinner at Persian terrace. it was really great experience . staff was very cautious and polite .very nice food especially falafel and ash e subzi soup. I
If you want to have good non veg starters here is the place. Really different taste and you will never be done. The taste is so good that you will want to come back again and again. 
This Halal restaurant is one of the best restaurants in Bangalore. It is a multi-cuisine restaurant. Interior is very clean and staff were excellent. Every type of food I tried was great.
Our favourite place for dinner. We love their chicken - grilled as well as special Barbeque chicken (sweetish). 
The food here is great. We had ordered for grilled chicken and Lamb Rayesh.
Usually have had delivery at diamond district at friends place n found the delivey fast
Went for lunch. A great food. Pepper barbeque was just too good. Biryani was also not bad. Overall great food.
Excellent south Indian food! Must try the vadas. The prices are reasonable as well. The problem is that the place gets very crowded often.
This coffee restaurant is best place to have early morning breakfasts and to energies body we have coffee shots also available.
This is one of the oldest places to have south Indian food in Bangalore. They have patented their recipe of chutney and has amazing idli, vada and coffee.
This well known place in the old charming neighborhood is an attraction offering a great taste of coffee . The faithfuls come here to snack and cup of filter coffee .
The place Brahmins is surely not to miss. our all time favourite cafe to satiate our hunger for typical idli chuney and vada.
High quality hygienic idli vada coffee . Near jnanodaya school its a very good place for having morning breakfast
The restaurant place was bit bit small but the food was good to taste and filter coffee is awesome there.
Sip a coffee, Have their famous Khara Bath and Idly Wada. A tiny place where you need to stand and eat the food , but truly great quality Food. I have been visiting since 2006.
I have been to this place more than 100 times and I have never got bored of it. They have a huge menu to select from and they have the Best burger in town.
The place is great for continental food.
They serve delicious Burgers and Pasta!!! The deserts are just too good.
The ambience is awesome. This place is famous for its burgers especially American Double Cheese Burger. Overall the place is nice.
We visited this place as a group of 8 for dinner over the weekend around 10:30 p.m. The place was buzzing with people! We ordered burgers, steaks and red velvet cake besides other desserts. The quantity is good and so is the quality! 
This place offers best in class buggers and other eateries . Only negative point is that , it does not have parking and on weekends we have to wait in line for almost 20-30 mins for getting a table .
Tried they open Joe burger, along with a chicken/lamb steak. Plus a chocolate shake. Everything was good!
its an amazing restraunt in kormangala. the ambience and the crowd is thumbs up. the menu and choices are also amazing. the portion is large. over all a really good experience. must try if your in kormangala and a foodie.
The food is great, I went with the Tons of Fun burger, which is a lamb burger with cheese and a fried egg. I hate to give the restaurant 4 stars because I think it is a place everyone traveling through should go to.
I m a regular customer of this place. Have one of the best deserts and snacks. Waiting for the seat for such a amazing food is worth it.
Superb desserts. Must visit. Helpful staff and owner is also interactive. Try the kahlua fantasy. Good options
Liked the burger options at this place. For me personally, 1 burger was not enough and 2 was too much :D Liked the vegetarian burger they had and ended up ordering 2. Recommended for a good evening with friends over burgers.
I visited truffles recently. Very good place and ultimate food. Service was excellent. Will visit soon again.
This place has the best burgers in Bengaluru (Bangalore). I'm a vegetarian and love this place as they have a wide range of dishes even for vegetarians. 
We visited truffles on friday ... usually it is packed up on weekends..Ambience i could not enjoy much but it was very crowded... we had to wait for some time to get table for 10... Food was really tasty.
Besides the wide choice of drinks and reasonably good food, the choice of live bands is an interesting option. Worth a visit. Acoustics are good.
You can definitely get one of the best burgers in town.. a bit pricey but should try once.. Nice ambience nice service.
We frequent Hard Rock cafe mainly because it's a very kid friendly place.
Hard Rock Cafe located at the Anil Kumble Circle in Bengaluru is famous for celebrity events. Usually I visit this place for events performed by celebrities.
Great time with live music. Starter was good. The famous burgers could be better. Great location. Good place to chill out. Will love to go back
Its really great experience. The staff's are courteous.iam sure that when ever i visits Bangalore i will go there i will recommend my friends and colleagues
Where we can get the snacks and other things with reasonable price with great taste. The service also very good.
I love hospitality and service.They serve American servings. Great music and amazing ambience. 
Its a relaxed lounge cafe. You can enjoy ur snacks and coffee whilst you work or chat. Brightly lit making it ideal for serious discussions. Good service
The definition of Marzipan was etched on to the front door - I drooled as childhood memories of the sweet, cloggy, wonder floated up. Come to Ulsoor for a piece of ''Spanakopita'' which is basically a Greek Spinach Pie
We visited Marzipan for lunch this afternoon. The place is nice and quiet. Good ambience. Warm hospitality. Very efficient. We had grilled sandwiches (omelette and chicken). Both made perfectly. Enjoyed the meal and ambience. Good place to eat. Go for it.
The cafe is very nice. Excellent ambiance. The food is good though a bit on pricey side. Service is quick and friendly.
Lovely selection of desserts. Must try the greek yoghurt like mango dessert- unique, healthy and yum.
Very nice cafe.. trendy decor.. we had a good time with friends over coffee and cold coffee, chai and iced teas. The strawberry cheesecake is yummy.. 
Predominantly greek food on offer but this is a great place to hang out. A good option to grab a quick bite too.The desserts in particular are enticing
a cute lil' café perfect for a quick lunch or iced tea with a piece of Victoria or walnut cake. newly launched, it does have a few teething issues but displays a promising start. 
We were celebrating a friend’s birthday here over lunch and had heard so much about Fava. We were not the least bit disappointed. The non vegetarian options are aplenty and really good but as are the vegetarian options!
We had starters and main course. The customer service was very good and quick. Food also very good and we had pleasant time there! Don’t miss it!
This has been an all time favorite of mine now. Excellent food, location and decent pricing (given the location).
Their selection of starters and mains is formidable and the taste, superb I enjoy their hummus and pita, soups and salads
Very very very good place to have food....and if you go there u much try "FALAFEL" this its awesome really....
We went here for lunch on a weekend. The ambiance is pleasant, the decor is bright and colorful. Both the food and the drinks menus were varied and interesting. We ordered a few cocktails and the mezze 'sharing' platter.
My husband and I are always craving Mediterranean food and we were very happy with Fava's selection.
It's a very nice place with amazing view of the adjoining buildings. Had cold coffee n green tea, was good. Nice ambiance.
place is inside ub city with clam environment only on weekdays. try something new thing, and new drink
This is a fusion India. Cuisine with European. Influence and great wine list . For the curious and different
First of all, i would like to say - dont miss it! It has a superb ambience, with a view of the world-class UB city towers, cool breeze
Amazing ambiance, very friendly staff and the presentation is also very nice. Tried 2 desserts which were ok but more than anything else, the place rocks.
Great ambience, friendly staff and great food. Lovely place for an evening out, specially weekends. Imported whisky is expensive. Go for mezzeh platter, hummus, tiger prawns with garlic, veg pizza....overall taste excellent.
A beautiful restaurant to enjoy some great Mediterranean food, I absolutely loved their Cryo-cocktails, the Morgan Colada is a must-try. They have an interesting menu with ingredients that are locally sourced and organically grown, they also have a liquid nitrogen ice cream counter outside.
Restaurants in UB city never fail you in food and experience. This one is no exception. Though it is a Mediterranean place we tried more of European food and was extremely good. The live salad was a great experience for the kids.
Went there for dinner and had a variety of appetizers that were prepared differently with a unique flavour and taste. Loved the lamb shank.
A lovely restaurant in UB city terrace,has both indoor and open seating with a live kitchen. 
What can one say of an experience that lingers in memory. How does one recommend one detail or dish from a long list of near perfection.
What delicious food!!! I ate the microgreens salad, chicken breast stuffed with caramelized onions and had vanilla ice cream scoop with crumbled oreo cookies. It was all so fresh, delicious and beautiful presentation as well. Service was good.
We visited Fava early evening on a long weekend Monday. Happy hour was on.....they had unlimited beer and sangria for 2 hrs which was a great deal ! Staffs were very friendly and they made sure that we had a good time there.
Super place for high quality italian & other Mediterranean food.Nice comfortable seating overlooking the UB city square where there are many restaurants.Fine dining but reasonable as compared to other premium restaurants
A relaxed place in UB City, for any of the 2 meals .. always like the ambience .. the music though can be a little loud, so need to request to be toned down .. otherwise food is great .. good to the Indian palette.. tried Spanakopita Spinach with Feta, tagine with couscous, Paneer/Vegetable Skewers and Falafel in pita pockets.. everything was good .. service polite and prompt and they have a kids menu as well!
Upon entering the restaurant, I felt like I was transported to a serene beach somewhere in Greece. The lovely music & the decor were very appropriate to the theme of the place. The food was incredibly good, my favourite would be the ravioli. The staff were very polite & the method of presenting certain dishes were somewhat fun to watch. We especially loved the complimentary chocolate truffles that came with the bill.
I loved the place and would surely go back there for the great food and the laid-back atmosphere.
Nice ambience and good menu. There are varieties for vegetarians too. Different food..but its yumm.. best is the chocolate which they serve at the end. It just melts in your mouth. Great starters and soup
Sister restaurant of Caperberry, now both at UB City as well. Mediterranean food and a good bar. Great for a relaxed evening
Food and service here was excellent. Food was cooked to perfection; both main and dessert. Wine and cocktails were also very good. This is a must if you're heading to UB City and have even the slightest interest in quality Mediterranean cuisine.
The bread sticks and sauce that come when you are seated are so delicious! The tenderloin and fish kabobs were fantastic, but the micro greens salad was the star! Made right at your table, you cannot get any fresher or more tasty! The bloody Mary's and virgin Mary's also hit the spot!
They served alcohol and wide variety of Mediterranean dishes. The service is spectacular.
 The staff is every knowledgeable, courteous and friendly. The service is quick and the portions of the food is humongous. Would definitely recommend it to people and will be going back there when I am in town next
on Friday nights you can definitely try it as there will a DJ playing and you can Dine, wine and Dance as well.
We had a very tasty dinner in the Karavalli restaurant. The food was excellent, the portion of the main course was so big that we could not try any dessert.
The atmosphere is very nice, especially if you wish a calm and relaxing dinner.
I would recommend the restaurant for both, private and business dinners.
I visit Bangalore every month and food at Karavalli has become a ritual. Appam and chicken stew are highly recommended. The place has a nice ambience and very hospitable staff. As far as I can remember this place has the best rasam I have ever tasted. Anthony is the best host one can have at Karavalli. Very polite, jovial and always happy to assist. Always looking forward to my visits here. 
Came here with a few coworkers one evening and really enjoyed our dinner. Sat out on the patio, which was a great experience. All of our food was very fresh and delicious, we tried a variety of starters and main courses and were pleased with everything. Will definitely visit again if I am back in town.
Easily one of the best seafood speciality restaurants I have dined. The ambience, the food, the service is all remarkable. A must visit place to enjoy good food.
I had a seafood thali and it was delicious - words cannot describe!!! Beyond that, the service was amazing - my waiter explained all the dishes, the chef came out to tell me about the dishes, and others came to talk to me admit the ingredients. You must come and try for yourself. I will surely be back to explore the menu. 
Went there with my friend for dinner. Mr Uday recommended us Malabar Prantha and chickpea and served it hot and in less time. The place too is so beautiful. It added to the great experience we had.
Excellent food and service! The thali was amazing and very satisfying, very good quantities and the thali is unlimited! 
Had the most incredible lunch at Karavelli. The seafood was divine and the service was superb. 
Chef Ramachandran served us with some amazing south indian dishes. The pineapple curry was divine. The outside seating is beautiful with a great atmosphere. Uday was really helpful recommending us the signature dishes. All in all a great experience. Highly 
Good food, even better ambience, and excellent service. Known for coastal food. 
Excellent ambience. Great service by Anthony. Tasty food, best place to celebrate. Moplah meen biriyani was good.
I had an amazing experience celebrating my birthday with my wife at Karavalli. The location and ambience is out of the world.
This place has over the years become a must visit for my family when we are in Banglore. The lip smacking food, serene atmosphere and wonderful service all make the meal a memorable experience. The coastal cuisine which being served is mouth watering.
We were at the karavalli restaurant and enjoyed very much from both the catamaran and seafood combinations for lunch. The food was delicious, service and atmosphere were also great. The restaurant is located in a lovely garden in the heart of bengaluru.
We had a very nice lunch here enjoying the great south west coastal cuisine and professional service.
Stayingin the hotel after a long travel we searched for easy options - and were totally surprised: we enjoyed not only most delicious South Indian Coastal Cuisine but also a very attentative and hospitable service in a nice garden abience.
All types of cruisine is good we have had a number of various items and all very good . It has a good play area for kids so kids enjoy themselves
Great ambience in this restaurant and I loved the food - a great variety and really tasty. Lots of mocktails/cocktails on offer. Nice large outdoor restaurant with lots of families enjoying themselves.
One of the good restaurant available in Bangalore,
There are many varieties of food with good quality and taste
Very good ambiance, lot of open space . Great place will love to go back specially for sea food. Service is excellent, and one can have private parties here. 
You have choice of both buffet lunch and a la carte. went ahead with buffet and have to admit as great value for money which works out to 500/- per head (net price).
Relished the Special seafood soup which was really well prepared. The Goan promfret curry was authentic.. This impacted the taste but still enjoyed it. The sweet dish called Bebianca was amazing too.
Dad wanted to sit out and have a beer and this seemed to fit the bill. Walking distance from the hotel made the choice a lot easier. A great variety of drinks and seafood. Energetic and helpful staff.
Awesome Seafood Restaurant which has everything in style the Display of Fishes and Service and Ambience is class apart.
Very less Goan restaurant in Bangalore but this is the best with great ambiance and typical Goan taste. 
If you love pan Asian food with some beer, this is the place to visit. The decor is done up well with lot of plants around. Their starters are spot on. Please have a reservation before visiting this place, as it gets packed at times.
Wonderful food. For an American visitor this place is super cute and the staff are great. Everything I️ tried was very tasty. Highly would recommend.
The food is really good and the service is rather quick. Vietnamese cuisine is hard to come by anyways and these guys do a great job at it.
I never try real Vietnamese restaurant but this place they do a really nice food I been with friends for dinner and I really loved, and the service very rapid, and the price really good...
If you love Vietnamese food, then this is the place and if you dont know what it is like, then you must visit.
We visited this place on Valentines day. Though it was crowded, the host ensured to get us a place on the first floor.
Amazing Mouth Watering Vietnamese dishes. Amazing service and decent ambiance. We tried the jungle fish curry that was yummy. Must try
They food is good and authentic
The restaurant was very crowded when we arrived and it took half an hour for us to get a table of 6 people. But the wait was worth it. We tried their Banh Cuon, Viet spare ribs and viet wings as appetizers
This is a fantastic place to eat out in the evening. True Taj Quality and Service. The place looks more like a Vietnamese resort restaurant....true to it’s name. Excellent soups, starters and main course. 
Used this for lunch time and evening drinks. Staff were friendly and very helpful. Very pleasant atmosphere and setting.
Very welcoming place to visit with kids. Excellent food and great ambience. Enjoyed and definitely recommended.
superb ambience and location...this place has some really good crowd on weekend nights... drinks are a bit steep but ok for that once in a while splurge!
Nice setting, next to a bar. Tasting menus are recommended. The meat/ seafood option was quite good. Don’t miss the shrimp curry with baguette. They customize the dishes as per your taste.
We loved the personalized care given by Sous Chef - Ankit Malhotra at Blue Ginger. The food was awesome, service was impeccable and decor was charming. had a great evening with my wife.
Excellent food choices whether you are eating alone or entertaining guest. Excellent service and very friendly staff
Its the story about ITC Windsor - The Raj Pavilion's Rogan Josh with Cheese Naan We were a group of 3 and we decided to go to this place.
Something for everyone. The staff went out of their way to ensure each individual need was met. Great to see so much attention lavished on the little ones so that the Parent had time to enjoy their meal.
This is a restaurant to come to with your closest family and friends. It's a happy mix of music, nostalgia, great service and gourmet food:-)! The evening jazz and oldies emanating from the bar next door adds to the relaxed grace of this place.
The breakfast and dinners are excellent in Raj Pavilion. You can easily find a lot to eat from breakfast and dinner buffet offerings.
Probably the best in Bangalore, it would not be complete without their Chef who treats every guest with tru Indian hospitality as if they were eating at his home. Breakfast, lunch, high tea and dinner are all outstanding !!!!
Thank you to the Chef for exchanging with guests in the restaurant. Excellent buffet from international to South Indian specialties! 
Had a great time during Christmas with my family and friends. Great service by the team. Real classy place. View is fantastic. Would love to go back there.
Excellent service and choice and quality of food. A very exceptional coffee shop with superb breakfast and huge choice of very good quality food. Hard to beat.
Excellent Cuisine, Service and En. Very Good Spread. Different types of Dishes. Wide choice of drinks/ Beverages.
The place is very clean and the ambiance too good. It was a great experience. Lots of smoothies, fresh fruit juices, lassi and so on. Fresh fruits and continental breakfast. We had lots of lots of south indian breakfast items like dosa, idli, puri and vada. Also was items like paratas of different kinds, lots of items in the bakery and of course coffee and tea.
I was recommended the "daal makni" . I admit it was finger licking good.
Perfect place for family get-together, excellent ambiance, food and service.
I visited today for dinner to celebrate the birthday of a friend. The food served was as awesome as the people who served it and equally good was the chef who prepared to food to it's delicious best. Very nice ambience with hospitable staff added to the whole experience. 
Fine restaurant. Amazing chef’s special dishes. The chicken korhigassi and biriyani was exceptional. 
Beautiful location, attentive staff. Breakfast buffet grand. Best Waffles I ever had. Dinner was also good. 
Wonderful food. Excellent service. Specially Sachin was very caring and proactive. It is a multicusine and options are wonderful
Nice ambience and food
The variety of food is great and the traditional Indian dishes are very good. 
The pavilion is cool and very luminous, which is ok during the day, but I found it too luminous at dinner time. I enjoyed a lot all different breakfast Indian options.
The restaurant offers a lovely ambience as well as food and service. Excellent choice and great variety also.
Great food, just the right mix of quiet yet busy in the morning, and fantastic personal attention and service by Chef Dhiren.
good ambience
the buffet spread is good, but not great
but the great service makes up for everything else... the 5 star rating is primarily for the service... makes your meal a memorable experience
Superb waitstaff and food. My waiter would always gently suggest an Indian dish and they never failed to impress. I appreciate that gesture so much as I may not have otherwise tried anything "out of the ordinary".
Very nice restaurant very comfortable, facing the pool and quite well organized. Breakfast has good options and i loved the customized juice the chef did for me."""
    mylist= get_sentences(reviews)
    sentences = []

    sentences.extend(get_sentences(reviews))
    #print sentences
    tokenized_sentences = [tokenize(sentence) for sentence in sentences]
    #print tokenized_sentences
    tagged_sentences = [pos_tag(sentence) for sentence in tokenized_sentences]
    #print tagged_sentences
    aspect= aspects_from_tagged_sents(tagged_sentences)
    #aspect = ['food', 'place', 'service', 'ambience', 'restaurant', 'staff', 'experience', 'dinner', 'breakfast', 'time']
    print aspect
    score_aspect(reviews, aspect)
    finaldict=aspect_opinions(reviews)
    #print finaldict





