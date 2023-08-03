from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    
    # path('NuevaTerapia/', views.NuevaTerapia, name='NuevaTerapia'),
    path('<str:paciente_id>/HistorialTerapias/NuevaTerapia/', views.NuevaTerapia, name='NuevaTerapia'),
    
    path('<str:id_paciente>/HistorialTerapias/', views.ListarTerapias, name='ListarTerapias'),
    
    # path('VerTerapia/<int:terapia_id>/', views.VerTerapia, name='VerTerapia'),
    
]