from django import forms
import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.http import request
from .models import Perfil

class MyUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


SIGNOS =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five")
)

class SignoZodiaco(forms.ModelForm):
        class Meta:
            model = Perfil
            fields = ['User', 'signo_zodiaco']

