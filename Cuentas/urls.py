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

]