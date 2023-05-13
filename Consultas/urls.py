from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [
    path('', views.index, name='index'),
    path('DetallesConsulta/<int:consulta_id>/', views.DetallesConsulta, name='DetallesConsulta'),
]