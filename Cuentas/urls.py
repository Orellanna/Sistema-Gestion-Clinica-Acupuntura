from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns = [
    #urls de acceso
    path('login/', views.Login,name='login'),
]