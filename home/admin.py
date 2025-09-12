from django.contrib import admin
from .models import EstudiantePublicador, EstudianteAutorizador, Publicacion

admin.site.register(EstudiantePublicador)
admin.site.register(EstudianteAutorizador)
admin.site.register(Publicacion)
