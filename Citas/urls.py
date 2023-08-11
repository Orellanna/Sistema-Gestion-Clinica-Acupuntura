from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    
    #urls libreria
    path('GestionCitas/', views.GestionCitas, name='GestionCitas'),
    path('RegistrarCitas/', views.RegistrarCitas, name='RegistrarCitas'),
  
    ]