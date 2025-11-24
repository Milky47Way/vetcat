"""
URL configuration for vetcat_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, breeds, breed, login_view, logout_view, register_view

urlpatterns = [
    path('home/', home, name="vatcat-home"),
    path('breeds/', breeds, name="models-breeds"),
    path('breed/<int:pk>', breed, name="models-breed"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('register/', register_view, name="register"),
]

app_name = "vatcat"

#python manage.py runserver
#cd vetcat_project

#http://127.0.0.1:8000/vetcat/home/

