from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [    
    #urls libreria
    path('GestionPacientes/', views.GestionPacientes,name='GestionPacientes'),
    path('datosPersonales/<str:id_paciente>/', views.DatosPersonales,name='DatosPersonales'),
    path('registrarPaciente/', views.Registrar, name='registrarPaciente'),
    path('editarPaciente/<str:id_paciente>/', views.EditarPaciente, name='editarPaciente'),
    path('eliminarPaciente/<str:id_paciente>/', views.EliminarPaciente, name='eliminarPaciente'),

]
