from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('gestionPacientes/', views.GestionPacientes),
    path('detallesConsulta/', views.DetallesConsulta),
]
