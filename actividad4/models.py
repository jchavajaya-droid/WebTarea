from django.db import models
from django.contrib.auth.models import User 

class Estudiante(models.Model):
    carnet = models.CharField(max_length=10, unique=True)
    nombre_completo = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre_completo} ({self.carnet})"

class Administrador(models.Model):
    nombre_completo = models.CharField(max_length=100)
    carrera = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)

    def __str__(self):
        return self.nombre_completo

class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publicaciones_creadas')
    autorizada = models.BooleanField(default=False)
    autorizado_por = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name='publicaciones_autorizadas')

    def __str__(self):
        return self.titulo
