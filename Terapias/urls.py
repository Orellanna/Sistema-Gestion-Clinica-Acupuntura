from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    
    # path('NuevaTerapia/', views.NuevaTerapia, name='NuevaTerapia'),
    path('<str:paciente_id>/HistorialTerapias/NuevaTerapia/', views.NuevaTerapia, name='NuevaTerapia'),
    
    path('<str:id_paciente>/HistorialTerapias/', views.ListarTerapias, name='ListarTerapias'),
    
    path('<str:id_paciente>/HistorialTerapias/DetallesTerapia/<str:terapia_id>/', views.DetallesTerapia, name='DetallesTerapia'),
    
    path('<str:id_paciente>/HistorialTerapias/EliminarTerapia/<str:terapia_id>/', views.EliminarTerapia, name='EliminarTerapia'),
    
    path('<str:paciente_id>/HistorialTerapias/DetallesTerapia/<str:terapia_id>/imprimir_terapia/', views.Imprimir_Terapia, name='Imprimir_Terapia'),
]