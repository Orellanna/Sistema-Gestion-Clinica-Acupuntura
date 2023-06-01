from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Cuentas.views import LoginView
from .views import HomePage,Login



urlpatterns = [
<<<<<<< HEAD
<<<<<<< HEAD
    #urls de acceso
    path('home/', HomePage, name='home'),
    path('administracion/', views.Administracion, name='administracion'),
    path('login/', Login, name='login-page'),
    path('Registro/', views.NuevoUsuario, name='registroUsuario'),
    path('GestionUsuarios/', views.GestionUsuarios, name='gestionUsuarios'),

]
=======
        path('home/', HomePage, name='home'),
=======
    path('home/', HomePage, name='home'),
>>>>>>> main
    path('administracion/', views.Administracion, name='administracion'),
    path('login/', Login, name='login-page'),
    path('cerrar_sesion/', views.cierre_sesion, name='cerrar_sesion'),
    path('Registro/', views.NuevoUsuario, name='registroUsuario'),
    path('GestionUsuarios/', views.GestionUsuarios, name='gestionUsuarios'),
<<<<<<< HEAD
    ]
>>>>>>> AV10001
=======
    path('verUsuario/<str:username>/',views.VerUsuario,name='verUsuario'),
    path('eliminarUsuario/<str:username>/', views.EliminarUsuario, name='eliminarUsuario'),
    path('editarUsuario/<str:username>/', views.EditarUsuario, name='editarUsuario'),
    ]
>>>>>>> main
