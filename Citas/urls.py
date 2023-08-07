from django.urls import path
from . import views
from django.contrib import admin
from Pacientes.models import Citas

urlpatterns = [
    path('', views.index, name='index'),
    
    #urls libreria
    path('Citas/', views.GestionCitas, name='GestionCitas'),
    path('Citas/IngresarCita', views.IngresarCita , name='IngresarCita'),
    path('Citas/NuevaCita', views.NuevaCita , name='NuevaCita' ),
    ]