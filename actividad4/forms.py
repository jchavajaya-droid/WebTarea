from django import forms
from .models import Estudiante, Administrador, Publicacion
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['carnet', 'nombre_completo', 'carrera', 'email']
        widgets = {
            'carnet': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['nombre_completo', 'carrera', 'correo']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'carrera': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PublicacionForm(forms.ModelForm):
    # Selección directa de estudiantes y administradores
    autor = forms.ModelChoiceField(
        queryset=Estudiante.objects.all(),
        label="Autor",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    autorizado_por = forms.ModelChoiceField(
        queryset=Administrador.objects.all(),
        label="Autorizado por",
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'autor', 'autorizado_por']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'contenido': forms.Textarea(attrs={'class': 'form-control'}),
        }
