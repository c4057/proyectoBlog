from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppBlog.models import Avatar 



class SemillaFormulario(forms.Form):

    nombre = forms.CharField()

class PlantaFormulario(forms.Form):
    nombre = forms.CharField()

class MacetaFormulario(forms.Form):
    nombre = forms.CharField()
    modelo = forms.IntegerField()     

class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta: 

        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

class FormularioEditar(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la Contraseña", widget=forms.PasswordInput)

    class Meta: 

        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]

class AvatarFormulario(forms.ModelForm): #permite crear un formulario a partir de un modelo que ya existe

    class Meta:

        model = Avatar
        fields = ["imagen"]

