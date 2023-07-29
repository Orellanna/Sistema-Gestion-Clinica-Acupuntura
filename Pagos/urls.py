from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Cuentas.views import LoginView
from Pagos.views import NuevoPago



urlpatterns = [
    path('NuevoPago/', views.NuevoPago, name='NuevoPago'),
    path('HistorialPagos/<str:paciente_id>/', views.ListarPagos, name='ListarPagos'),
    path('HistorialPagos/<str:paciente_id>/DetallesPago/<str:pago_id>/', views.DetallesPago, name='DetallesPago'),

    ]