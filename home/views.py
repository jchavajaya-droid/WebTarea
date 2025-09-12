from django.shortcuts import render
from .models import Publicacion

def inicio(request):
    return render(request, 'inicio.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def administradores(request):
    return render(request, 'administradores.html')

def acerca(request):
    return render(request, 'acerca.html')

def publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})