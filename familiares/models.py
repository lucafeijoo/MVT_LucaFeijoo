from turtle import color
from django.db import models

class familiares(models.Model):
    nombre = models.CharField(max_length=64)
    fecha_nacimiento = models.DateField()
    altura = models.IntegerField()
