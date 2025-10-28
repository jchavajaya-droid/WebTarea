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
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)  # ← este campo
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    autorizada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} - {self.autor.username}"
