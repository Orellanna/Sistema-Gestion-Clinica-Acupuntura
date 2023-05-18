from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    path('', views.index, name='index'),
    
    #urls libreria
    path('GestionPacientes/', views.GestionPacientes,name='GestionPacientes'),
    path('detallesConsulta/', views.DetallesConsulta,name='DetallesConsulta'),
     path('datosPersonales/', views.DatosPersonales,name='DatosPersonales'),
    ##Borrar lo de abajo antes de subir cambio - Kevin
    path('registrarPaciente/', views.Registrar,name='registrarPaciente'),

]
