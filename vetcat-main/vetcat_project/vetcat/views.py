from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm

from .models import Breed


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

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect('vetcat:login')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form':form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('vatcat:vatcat-home')  # змінити на вашу сторінку
            else:
                return render(request, 'login.html', {
                    'form': form,
                    'error': 'Невірний логін або пароль'
                })
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('vetcat:login')






#python manage.py runserver