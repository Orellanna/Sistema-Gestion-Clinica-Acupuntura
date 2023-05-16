from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:paciente_id>/HistorialConsultas/NuevaConsulta/', views.NuevaConsulta, name='NuevaConsulta'),
    path('<int:paciente_id>/HistorialConsultas/DetallesConsulta/<int:consulta_id>/', views.DetallesConsulta, name='DetallesConsulta'),
    path('<int:paciente_id>/HistorialConsultas/', views.ListarConsultas, name='ListarConsultas'),
]