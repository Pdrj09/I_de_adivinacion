from django.db import models
from django.db.models.fields import CharField, DateField
from django.contrib.auth.models import User
# Create your models here.
class tarotistas(models.Model):
    nombre = models.CharField(max_length = 15)
    especialidades = models.CharField(max_length = 500)
    actividades = models.CharField(max_length = 500)
    imagen = models.ImageField(upload_to="static/images/tarotistas", null = True, blank = True)

class eventos(models.Model):
    fecha = models.DateField()
    acctividad = models.CharField(max_length = 500)


SIGNOS =(
    ("Aries", "Aries"),
    ("Tauro", "Tauro"),
    ("Géminis", "Géminis"),
    ("Cáncer", "Cáncer"),
    ("Leo", "Leo"),
    ("Virgo", "Virgo"),
    ("Libra", "Libra"),
    ("Escorpio", "Escorpio"),
    ("Sagitario", "Sagitario"),
    ("Capricornio", "Capricornio"),
    ("Acuario", "Acuario"),
    ("Piscis", "Piscis"),
)

class Perfil(models.Model):
    User = models.OneToOneField(User, on_delete = models.CASCADE)
    signo_zodiaco = models.CharField(max_length = 11, choices = SIGNOS)