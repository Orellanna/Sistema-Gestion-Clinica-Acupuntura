from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Cuentas.views import LoginView
from Pagos.views import NuevoPago



urlpatterns = [
    path('NuevoPago/<str:paciente_id>/', views.NuevoPago, name='NuevoPago'),
    path('HistorialPagos/<str:paciente_id>/', views.ListarPagos, name='ListarPagos'),
    path('HistorialPagos/<str:paciente_id>/<str:consulta_id>/DetallesPago/<int:pago_id>/', views.DetallesPago, name='DetallesPago'),
<<<<<<< Updated upstream
    path('HistorialPagos/<str:paciente_id>/EditarPago/<str:pago_id>/', views.EditarPago, name='EditarPago'),

    ]
=======
    path('HistorialPagos/<str:paciente_id>/EditarPago/<int:pago_id>/', views.EditarPago, name='EditarPago'),
    path('HistorialPagos/<str:paciente_id>/EliminarPago/<int:pago_id>/', views.EliminarPago, name='EliminarPago'),
    path('HistorialPagos/<str:paciente_id>/DetallesPago/<int:pago_id>/', views.Imprimir_Pago, name='Imprimir_Pago'),
    
]
>>>>>>> Stashed changes
