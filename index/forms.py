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




class SignoZodiaco(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['signo_zodiaco']
        