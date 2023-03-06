from django.db import models

# Create your models here.

class Motosierra(models.Model):
        modelo = models.CharField(max_length=64)
        descripcion = models.CharField(max_length=128)
        precio = models.IntegerField()

        def __str__(self):
                return f"{self.modelo}: {self.descripcion} - {self.precio}"

class Desbrozadora(models.Model):
        modelo = models.CharField(max_length=64)
        descripcion = models.CharField(max_length=128)
        precio = models.IntegerField()

        def __str__(self):
                return f"{self.modelo}: {self.descripcion} - {self.precio}"

class Cortacesped(models.Model):
        modelo = models.CharField(max_length=64)
        descripcion = models.CharField(max_length=128)
        precio = models.IntegerField()

        def __str__(self):
                return f"{self.modelo}: {self.descripcion} - {self.precio}"
