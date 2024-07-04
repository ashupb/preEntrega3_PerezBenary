from django.db import models

class Collares(models.Model):
    tipo = models.CharField(max_length=50)
    tamanio = models.CharField(max_length=50)
    precio = models.IntegerField()

class Alimentacion(models.Model):
    tipo = models.CharField(max_length=60)
    tamanio = models.CharField(max_length=50)
    precio = models.IntegerField()

class Confort(models.Model):
    tipo = models.CharField(max_length=50)
    precio = models.IntegerField()
 
