from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [
    path('', views.index, name='index'),
    
    #urls libreria
    path('Inventario/', views.ListarInventario , name='GestionInventario'),
    path('Inventario/RegistrarProducto/', views.RegistrarProducto, name='RegistrarProducto'),
    path('Inventario/DetallesProducto/<int:id_suministro>/', views.DetallesProducto, name='DetallesProducto'),
    path('Inventario/EditarProducto/<int:id_suministro>/', views.EditarProducto, name='EditarProducto'),
    path('Inventario/EliminarProducto/<int:id_suministro>/', views.EliminarProducto, name='EliminarProducto'),
]