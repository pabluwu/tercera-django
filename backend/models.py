from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Bombero(AbstractUser):

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('primer_nombre', 'primer_apellido', 'segundo_apellido', 'rut', 'cargo','username')

    id = models.AutoField(primary_key=True, unique=True)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    rut = models.CharField(max_length=9, unique=True)
    telefono = models.CharField(max_length=9, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    cargo = models.CharField(max_length=30)

class Citacion(models.Model):

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=30, blank=None)
    fecha = models.DateTimeField(blank=None)
    descripcion = models.TextField(max_length=250, blank=None)