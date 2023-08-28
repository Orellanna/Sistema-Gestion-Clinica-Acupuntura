from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    
    path('<str:paciente_id>/HistorialConsultas/NuevaConsulta/', views.NuevaConsulta, name='NuevaConsulta'),
    
    path('<str:paciente_id>/HistorialConsultas/DetallesConsulta/<str:consulta_id>/', views.DetallesConsulta, name='DetallesConsulta'),
    
    path('<str:paciente_id>/HistorialConsultas/EditarConsulta/<str:consulta_id>/', views.EditarConsulta, name='EditarConsulta'),
    
    path('<str:paciente_id>/HistorialConsultas/', views.ListarConsultas, name='ListarConsultas'),
    
    path('<str:paciente_id>/HistorialConsultasDeshabilitadas/', views.ListarConsultasDeshabilitadas, name='ListarConsultasDesabilitadas'),

    
    path('<str:paciente_id>/HistorialConsultas/EliminarConsulta/<str:consulta_id>/', views.EliminarConsulta, name='EliminarConsulta'),
    
    path('<str:paciente_id>/HistorialConsultas/DetallesConsulta/<str:consulta_id>/generar_reporte_pdf/', views.generar_reporte_pdf, name='GenerarReportePDF'),
    
    path('reactivarConsulta/<str:paciente_id>/<str:consulta_id>/', views.ReactivarConsulta, name='reactivarConsulta'),

    
    path('construccion/', views.EnConstruccion, name='construccion'),

]