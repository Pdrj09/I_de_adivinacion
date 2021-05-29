from django.db import models
from django.db.models.fields import CharField, DateField
# Create your models here.
class tarotistas(models.Model):
    nombre = models.CharField(max_length = 15)
    especialidades = models.CharField(max_length = 500)
    actividades = models.CharField(max_length= 500)
    imagen = models.ImageField(upload_to="static/images/tarotistas", null=True, blank=True)

class eventos(models.Model):
    fecha = models.DateField()
    acctividad = models.CharField(max_length= 500)

