from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    #urls libreria
    path('Reportes/', views.ListarReportes,name='reportes'),

]
