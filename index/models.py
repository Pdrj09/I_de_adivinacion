from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.
class tarotistas(models.Model):
    nombre = models.CharField(max_length = 15)
    especialidades = CharField(max_length = 500)
    actividades = CharField(max_length= 500)

class eventos(models.Model):
    fecha = DateField()
    acctividad = CharField(max_length= 500)
