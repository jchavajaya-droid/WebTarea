from django import forms
from .models import Estudiante, Administrador

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['carnet', 'nombre_completo', 'carrera', 'email']

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre_completo', 'carrera', 'correo']
