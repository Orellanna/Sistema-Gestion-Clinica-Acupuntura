from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Cuentas.views import LoginView
from Pagos.views import NuevoPago



urlpatterns = [
    path('NuevoPago/', views.NuevoPago, name='NuevoPago'),

    ]