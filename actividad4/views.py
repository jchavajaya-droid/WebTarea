from django.shortcuts import render, redirect, get_object_or_404
from .models import Estudiante, Administrador
from .forms import EstudianteForm, AdministradorForm, RegistroUsuarioForm
from django.contrib.auth import login


# ---------- ESTUDIANTES ----------    
def inicio(request):
    return render(request, 'inicio.html')

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()  
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes})

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'agregar_editar_estudiantes.html', {'form': form, 'titulo': 'Agregar Estudiante'})

def editar_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'agregar_editar_estudiantes.html', {'form': form, 'titulo': 'Editar Estudiante'})

def ver_estudiante(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    return render(request, 'ver_estudiante.html', {'estudiante': estudiante})



# ---------- ADMINISTRADORES ----------
def lista_administradores(request):
    administradores = Administrador.objects.all() 
    return render(request, 'administradores.html', {'administradores': administradores})

def agregar_administrador(request):
    if request.method == 'POST':
        form = AdministradorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_administradores')
    else:
        form = AdministradorForm()
    return render(request, 'agregar_editar_administrador.html', {'form': form, 'titulo': 'Agregar Administrador'})

def editar_administrador(request, id):
    admin = get_object_or_404(Administrador, id=id)
    if request.method == 'POST':
        form = AdministradorForm(request.POST, instance=admin)
        if form.is_valid():
            form.save()
            return redirect('lista_administradores')
    else:
        form = AdministradorForm(instance=admin)
    return render(request, 'agregar_editar_administrador.html', {'form': form, 'titulo': 'Editar Administrador'})

def ver_administrador(request, id):
    admin = get_object_or_404(Administrador, id=id)
    return render(request, 'ver_administrador.html', {'administrador': admin})



#---------- REGISTRO DE USUARIOS ----------
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)  
            return redirect('inicio')  
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registrar_usuario.html', {'form': form})