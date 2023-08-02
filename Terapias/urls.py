from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    
    path('NuevaTerapia/', views.NuevaTerapia, name='NuevaTerapia'),
    path('ListarTerapias/<str:id_paciente>/', views.ListarTerapias, name='ListarTerapias'),
    path('VerTerapia/<int:terapia_id>/', views.VerTerapia, name='VerTerapia'),
    
    
]