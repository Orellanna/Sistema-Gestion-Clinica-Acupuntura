from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Cuentas.views import LoginView
from .views import HomePage,Login,logout


urlpatterns = [
    #urls de acceso
    path('home/', HomePage, name='home'),
    path('login/', Login, name='login-page'),
    path('Registro/', views.Registro,name='Registro'),
    path('logout/', views.logout, name='logout'),
   
]