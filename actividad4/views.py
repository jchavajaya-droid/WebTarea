from django.shortcuts import render
from .models import Publicacion

def inicio(request):
    return render(request, 'inicio.html')

def acerca(request):
    return render(request, 'acerca.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def administradores(request):
    return render(request, 'administradores.html')

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_publicaciones')  # más adelante crearemos esta vista
    else:
        form = PublicacionForm()
    return render(request, 'actividad4/crear_publicacion.html', {'form': form})

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()  # Trae todas las publicaciones
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})