from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('<str:paciente_id>/HistorialConsultas/NuevaConsulta/', views.NuevaConsulta, name='NuevaConsulta'),
    path('<str:paciente_id>/HistorialConsultas/DetallesConsulta/<str:consulta_id>/', views.DetallesConsulta, name='DetallesConsulta'),
    path('<str:paciente_id>/HistorialConsultas/', views.ListarConsultas, name='ListarConsultas'),
]