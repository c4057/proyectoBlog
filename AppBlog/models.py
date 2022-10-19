from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Semillas(models.Model):
    def __str__(self):

        return f"Nombre: {self.nombre}"

    nombre = models.CharField(max_length=60)

class Plantas(models.Model):
    def __str__(self):

        return f"Nombre: {self.nombre}"

    nombre = models.CharField(max_length=60)

class Macetas(models.Model):

    def __str__(self):

        return f"Nombre: {self.nombre} ------ Modelo:{self.modelo}"

    nombre = models.CharField(max_length=60)
    modelo = models.IntegerField()

class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)    