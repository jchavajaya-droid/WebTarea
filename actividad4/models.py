from django.db import models

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


