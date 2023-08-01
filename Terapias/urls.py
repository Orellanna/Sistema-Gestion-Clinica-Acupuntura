from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    
    path('NuevaTerapia/', views.NuevaTerapia, name='NuevaTerapia'),
    
]