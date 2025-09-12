from django.db import models

class EstudiantePublicador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    carrera = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class EstudianteAutorizador(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    publicador = models.ForeignKey(EstudiantePublicador, on_delete=models.CASCADE)
    autorizador = models.ForeignKey(EstudianteAutorizador, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo
