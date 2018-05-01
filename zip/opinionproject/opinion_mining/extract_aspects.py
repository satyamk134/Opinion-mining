#!/usr/bin/env python
# coding=utf-8

"""
File for aspect extraction functions
"""

import nltk
import sys

from collections import Counter
from nltk.corpus import stopwords

from external.my_potts_tokenizer import MyPottsTokenizer

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


def pos_tag_stanford(toked_sentence):
	"""
	INPUT: list of strings
	OUTPUT: list of tuples8qfa

	Given a tokenized sentence, return 
	a list of tuples of form (token, POS)
	where POS is the part of speech of token
	"""

	from nltk.tag.stanford import POSTagger
	st = POSTagger('/home/satyam/zip/opinionproject/opinion_mining/resources/english-bidirectional-distsim.tagger',
               '/home/satyam/zip/opinionproject/opinion_mining/resources/stanford-postagger.jar')

	return st.tag(toked_sentence)


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


def demo_aspect_extraction(): 
	"""
	Demo the aspect extraction functionality on one restaurant
	"""

	from main import read_data, get_reviews_for_business, extract_aspects

	#TEST_BIZ_ID = 's1dex3Z3QoqiK7V-zXUgAw'

	print "Reading data..."
	#df = read_data()
	print "Done."

	#BIZ_NAME = str(df[df.business_id==TEST_BIZ_ID]['name'].iloc[0])


	print "Getting reviews for"# %s (ID = %s)" % (BIZ_NAME, TEST_BIZ_ID)
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
I visited hole in wall cafe with my son.Breakfast was tasty,delicious and very healthy.Ambience was excellent.I enjoyed a lot."""

	print "Done."

	print "Extracting aspects..."
	aspects = extract_aspects(reviews)


	print "Done."

	print "==========="
	#print "Aspects for %s:" % BIZ_NAME
	for i,aspect in enumerate(aspects):
		print str(i) + ". " + aspect


if __name__ == "__main__":
	demo_aspect_extraction()






