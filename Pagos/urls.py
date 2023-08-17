from django.urls import path
from . import views

urlpatterns = [
    path('HistorialPagos/NuevoPago/<str:paciente_id>/', views.NuevoPago, name='NuevoPago'),
    path('HistorialPagos/<str:paciente_id>/', views.ListarPagos, name='ListarPagos'),
    path('HistorialPagos/<str:paciente_id>/<str:consulta_id>/DetallesPago/<int:pago_id>/', views.DetallesPago, name='DetallesPago'),
    path('HistorialPagos/<str:paciente_id>/EditarPago/<int:pago_id>/', views.EditarPago, name='EditarPago'),
    path('HistorialPagos/<str:paciente_id>/EliminarPago/<int:pago_id>/', views.EliminarPago, name='EliminarPago'),
    path('HistorialPagos/<str:paciente_id>/DetallesPago/<int:pago_id>/imprimir_pago/', views.Imprimir_Pago, name='Imprimir_Pago')

]
