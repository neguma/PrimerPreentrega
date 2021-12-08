from django.db import models

# Create your models here.

class guitarra(models.Model):
    marca = models.CharField(max_length=15)
    modelo = models.CharField(max_length=15)
    cant_cuerdas = models.IntegerField()

class mastil(models.Model):
    madera=models.CharField(max_length=15)
    largo=models.IntegerField()
    trastes=models.IntegerField()

class cuerdas(models.Model):
    marca=models.CharField(max_length=15)
    grosor=models.IntegerField()
    tipo=models.CharField(max_length=15)
