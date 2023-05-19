from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from Cuentas.views import LoginView
from .views import HomePage,Login

urlpatterns = [
    #urls de acceso
    path('home/', HomePage, name='home'),
    path('login/', Login, name='login-page'),
]