from django.urls import path
from . import views
from django.contrib import admin



urlpatterns = [    
    #urls libreria
    path('Inventario/', views.ListarInventario , name='GestionInventario'),
    path('Inventario/RegistrarProducto/', views.RegistrarProducto, name='RegistrarProducto'),
    path('Inventario/DetallesProducto/<str:id_suministro>/', views.DetallesProducto, name='DetallesProducto'),
    path('Inventario/EditarProducto/<str:id_suministro>/', views.EditarProducto, name='EditarProducto'),
    path('Inventario/EliminarProducto/<str:id_suministro>/', views.EliminarProducto, name='EliminarProducto'),
]