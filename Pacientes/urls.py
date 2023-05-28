from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    path('', views.index, name='index'),
    
    #urls libreria
    path('GestionPacientes/', views.GestionPacientes,name='GestionPacientes'),
    path('detallesConsulta/', views.DetallesConsulta,name='DetallesConsulta'),
    path('datosPersonales/<str:id_paciente>/', views.DatosPersonales,name='DatosPersonales'),
    path('registrarPaciente/', views.Registrar,name='registrarPaciente'),
    path('<str:paciente_id>/GestionPacientes/', views.GestionPacientes, name='GestionPacientes'),
    ##path('editarPaciente/', views.EditarPaciente,name='EditarPaciente'),
    path('<str:paciente_id>/datosPersonales/editarPaciente/', views.EditarPaciente, name='EditarPaciente'),


]
