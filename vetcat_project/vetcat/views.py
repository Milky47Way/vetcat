from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import import render
from models import Breed
# Create your views here.

def home(request):
    return HttpResponse ("Welcome!")
    return render(request, 'home.html')

def breeds(request):
    breeds_obj = Breed.objects.all()
    return HttpResponse(breeds_obj)

def breed(request, pk):
    breed_obj = Breed.objects.filter(id=pk)
    return HttpResponse(breed_obj)


