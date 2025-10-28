from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Estudiante, Administrador, Publicacion
from .forms import EstudianteForm, AdministradorForm, RegistroUsuarioForm, PublicacionForm

# ---------- ESTUDIANTES ----------
def inicio(request):
    return render(request, 'inicio.html')

def lista_estudiantes(request):
    filtro = request.GET.get('filtro', '').strip()
    if filtro:
        estudiantes = Estudiante.objects.filter(
            Q(nombre_completo__icontains=filtro) |
            Q(carrera__icontains=filtro) |
            Q(carnet__icontains=filtro)
        )
    else:
        estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes.html', {'estudiantes': estudiantes, 'filtro': filtro})

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


# ---------- PUBLICACIONES ----------
@login_required
def crear_publicaciones(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            # Asignamos el usuario logueado como autor
            publicacion.autor = request.user
            publicacion.save()
            return redirect('publicaciones')  # Redirige a la lista de publicaciones
    else:
        form = PublicacionForm()
    
    return render(request, 'crear_publicaciones.html', {'form': form})

@login_required
def publicaciones(request):
    """Mostrar publicaciones según usuario"""
    if request.user.is_staff:
        publicaciones = Publicacion.objects.all()
    else:
        publicaciones = Publicacion.objects.filter(autorizada=True)
    return render(request, 'publicaciones.html', {'publicaciones': publicaciones})

@staff_member_required
def lista_publicaciones_pendientes(request):
    """Admin ve publicaciones pendientes de autorización"""
    publicaciones = Publicacion.objects.filter(autorizada=False)
    return render(request, 'autorizar_publicaciones.html', {'publicaciones': publicaciones})

@staff_member_required
def autorizar_publicaciones(request, pub_id):
    """Admin autoriza una publicación"""
    publicacion = get_object_or_404(Publicacion, id=pub_id)
    publicacion.autorizada = True
    publicacion.autorizado_por = request.user
    publicacion.save()
    return redirect('lista_publicaciones_pendientes')


# ---------- ADMINISTRADORES ----------
def lista_administradores(request):
    filtro = request.GET.get('filtro', '').strip()
    if filtro:
        administradores = Administrador.objects.filter(
            Q(nombre_completo__icontains=filtro) |
            Q(carrera__icontains=filtro) |
            Q(correo__icontains=filtro)
        )
    else:
        administradores = Administrador.objects.all()
    return render(request, 'lista_administradores.html', {'administradores': administradores, 'filtro': filtro})

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
    administrador = get_object_or_404(Administrador, id=id)
    if request.method == 'POST':
        form = AdministradorForm(request.POST, instance=administrador)
        if form.is_valid():
            form.save()
            return redirect('lista_administradores')
    else:
        form = AdministradorForm(instance=administrador)
    return render(request, 'agregar_editar_administrador.html', {'form': form, 'titulo': 'Editar Administrador'})

def ver_administrador(request, id):
    administrador = get_object_or_404(Administrador, id=id)
    return render(request, 'ver_administrador.html', {'administrador': administrador})


# ---------- REGISTRO DE USUARIOS ----------
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
