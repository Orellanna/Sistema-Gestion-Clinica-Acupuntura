from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.ListarCitas, name='ListarCitas'),
    path('HistorialCitas/', views.HistorialCitas, name='HistorialCitas'),
    path('CrearCita/', views.CrearCita, name='CrearCita'),  # Agrega esta línea para la creación de citas
    path('EditarCita/<int:cita_id>/', views.EditarCita, name='EditarCita'),
    path('EliminarCita/<int:cita_id>/', views.EliminarCita, name='EliminarCita'),
    path('VerCita/<int:cita_id>/', views.VerCita, name='VerCita'),
    path('VerCita/<int:cita_id>/imprimir_cita/', views.Imprimir_Cita, name='Imprimir_cita')
]