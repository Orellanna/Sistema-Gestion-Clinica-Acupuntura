from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Pacientes import views
from Consultas import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pacientes.urls')),
    path('', include('Consultas.urls')),
]
