from django.contrib import admin
from .models import Administrador, Estudiante  # importa tus modelos

# Registra los modelos para que aparezcan en el admin
admin.site.register(Administrador)
admin.site.register(Estudiante)
