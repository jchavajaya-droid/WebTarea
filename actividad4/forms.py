from django import forms
from .models import Estudiante, Administrador
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # ✅ ESTA LÍNEA ES LA CLAVE

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['carnet', 'nombre_completo', 'carrera', 'email']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre_completo', 'carrera', 'correo']

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
