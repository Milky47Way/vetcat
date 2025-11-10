from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from vetcat.models import Breed
# Create your views here.

def home(request):
    # return HttpResponse ("Welcome!")
    return render(request, 'home.html')

def breeds(request):
    breeds_obj = Breed.objects.all()
    context = {'breeds': breeds_obj}
    return render(request, 'breeds.html', context)
    #return HttpResponse(breeds_obj)

def breed(request, pk):
    breed_obj = Breed.objects.filter(id=pk).first()
    #return HttpResponse(breed_obj)
    context = {'breed': breed_obj}
    return render(request, 'breed.html', context)
#python manage.py runserver