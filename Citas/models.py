from datetime import date
from django.db import models
import base64

# Create your models here.

class Cita(models.Model):
    id_cita = models.CharField(primary_key=True, max_length=10)