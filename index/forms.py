from django import forms
import django
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.http import request
from .models import Perfil


class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, 254 caracteres como máximo y debe ser válido.')
    class Meta:
        model = User
        #fields['username'].widget = forms.TextInput(attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de usuario'})
        fields = ['username', 'email', 'password1', 'password2']
        
        def celan_email(self):
            email = self.cleaned_data.get('email')
            if not email:
                raise forms.ValidationError('Email no puede estar vacío.')
            return email


class SignoZodiaco(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['signo_zodiaco']
        