from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Cuentas.views import LoginView
from .views import HomePage,Login



urlpatterns = [
    #urls de acceso
    path('home/', HomePage, name='home'),
    path('administracion/', views.Administracion, name='administracion'),
    path('login/', Login, name='login-page'),
    path('Registro/', views.NuevoUsuario, name='registroUsuario'),
    path('GestionUsuarios/', views.GestionUsuarios, name='gestionUsuarios'),
    path('cerrar_sesion/', views.cierre_sesion, name='cerrar_sesion'),
    path('verUsuario/<str:username>/',views.VerUsuario,name='verUsuario'),
    path('eliminarUsuario/<str:username>/', views.EliminarUsuario, name='eliminarUsuario'),
    path('editarUsuario/<str:username>/', views.EditarUsuario, name='editarUsuario'),
<<<<<<< HEAD
]
=======
    path('ListarPacientesDeshabilitados/', views.ListarPacientesDeshabilitados, name='listarPacientesDeshabilitados'),
    path('habilitarPaciente/<str:paciente_id>/', views.HabilitarPaciente, name='habilitarPaciente'),
    ]
>>>>>>> main
