from django.shortcuts import render
from forms import myForm
from models import *

def index(request):
    return render(request, 'myapp/index.html')

def submitted(request):
   # RestaurantName=" sfsfasda"
    if request.method == "POST":
        MyLoginForm = myForm(request.POST)
        if MyLoginForm.is_valid():
            name = MyLoginForm.cleaned_data['tags']
        else:
            name="not found"
    else:
        MyLoginForm = myForm()
    imgpath="myapp/img/" +name+".jpeg"
    foodimg="myapp/img/"+name+"food.jpeg"
    modelObject=restaurent.objects.get(name=name)
    desc=modelObject.review_text
    return render(request, 'myapp/hotelPage.html', { "name": name,"imgpath":imgpath,"desc":desc,"foodimg":foodimg })





