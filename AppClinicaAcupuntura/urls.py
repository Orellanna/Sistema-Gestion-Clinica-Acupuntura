from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from Pacientes import views
from Consultas import views
from Cuentas import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Pacientes.urls')),
    path('', include('Consultas.urls')),
    path('',include('Cuentas.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
