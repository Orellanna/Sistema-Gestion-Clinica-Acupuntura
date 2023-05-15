from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:paciente_id>/HistorialConsultas/', views.ListarConsultas, name='ListarConsultas'),
    path('<int:paciente_id>/HistorialConsultas/NuevaConsulta/', views.NuevaConsulta, name='NuevaConsulta'),
    #path('NuevaConsulta/<int:paciente_id>/', views.NuevaConsulta, name='NuevaConsulta'),
    path('DetallesConsulta/<int:consulta_id>/', views.DetallesConsulta, name='DetallesConsulta'),
]