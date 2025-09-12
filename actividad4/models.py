from django.db import models
from django.contrib.auth.models import User

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    carnet = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} ({self.carnet})"


class Autorizador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    cargo = models.CharField(max_length=50)  # Ejemplo: "Coordinador de publicaciones"

    def __str__(self):
        return f"{self.nombre} - {self.cargo}"


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    autor = models.ForeignKey(Autorizador, on_delete=models.CASCADE)
    autorizado_por = models.ForeignKey(Autorizador, related_name="autorizaciones", on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo