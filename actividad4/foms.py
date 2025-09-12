# actividad4/forms.py
from django import forms
from .models import Publicacion, Estudiante

class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'contenido', 'autor', 'autorizado_por']

    # Opcional: filtrar solo ciertos estudiantes como autorizadores
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['autor'].queryset = Estudiante.objects.all()
        self.fields['autorizado_por'].queryset = Estudiante.objects.all()
