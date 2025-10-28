from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Estudiante, Administrador, Publicacion
from .forms import EstudianteForm, AdministradorForm, RegistroUsuarioForm, PublicacionForm
from django.contrib.auth import login



# ---------- ESTUDIANTES ----------    
def inicio(request):
    return render(request, 'inicio.html')

def lista_estudiantes(request):
    filtro = request.GET.get('filtro', '')  # obtiene el texto del campo de búsqueda
    if filtro:
        estudiantes = Estudiante.objects.filter(
            nombre_completo__icontains=filtro
        ) | Estudiante.objects.filter(
            carrera__icontains=filtro
        ) | Estudiante.objects.filter(
            carnet__icontains=filtro
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

def crear_publicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.estudiante = request.user
            publicacion.save()
            return redirect('mis_publicaciones')
    else:
        form = PublicacionForm()
    return render(request, 'crear_publicacion.html', {'form': form})



# ---------- ADMINISTRADORES ----------
def lista_administradores(request):
    filtro = request.GET.get('filtro', '').strip()  # obtiene el texto del campo de búsqueda y elimina espacios
    if filtro:
        administradores = Administrador.objects.filter(
            Q(nombre_completo__icontains=filtro) |
            Q(carrera__icontains=filtro) |
            Q(correo__icontains=filtro) |
            Q(carrera__icontains=filtro)
        )
    else:
        administradores = Administrador.objects.all()
    return render(
        request,
        'lista_administradores.html', 
        {'administradores': administradores, 'filtro': filtro}
        )

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

def administrar_publicaciones(request):
    publicaciones = Publicacion.objects.filter(aprobada=False)
    if request.method == 'POST':
        publicacion_id = request.POST.get('publicacion_id')
        publicacion = Publicacion.objects.get(id=publicacion_id)
        publicacion.aprobada = True
        publicacion.save()
        return redirect('administrar_publicaciones')
    return render(request, 'administrar_publicaciones.html', {'publicaciones': publicaciones})

def es_admin(user):
    return user.is_staff

def autorizar_publicacion(request, pub_id):
    if request.user.is_staff:
        pub = get_object_or_404(Publicacion, id=pub_id)
        pub.autorizada = True
        pub.save()
    return redirect('publicaciones')  # redirige a la lista de publicaciones

def publicaciones(request):
    # Estudiantes solo ven publicaciones autorizadas
    if request.user.is_staff:
        publicaciones = Publicacion.objects.all()  # Admin ve todas
    else:
        publicaciones = Publicacion.objects.filter(autorizada=True)
    
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            pub = form.save(commit=False)
            pub.autor = request.user
            pub.save()
            return redirect('publicaciones')
    else:
        form = PublicacionForm()
    
    context = {'publicaciones': publicaciones, 'form': form}
    return render(request, 'publicaciones.html', context)

def crear_o_editar_publicacion(request, pub_id=None):
    if pub_id:
        pub = get_object_or_404(Publicacion, id=pub_id)
        if request.user != pub.autor and not request.user.is_staff:
            return redirect('administrar_publicaciones')
    else:
        pub = None

    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=pub)
        if form.is_valid():
            nueva_pub = form.save(commit=False)
            if not pub:  # Si es creación
                nueva_pub.autor = request.user
            nueva_pub.save()
            return redirect('administrar_publicaciones')
    else:
        form = PublicacionForm(instance=pub)

    return render(request, 'crear_publicaciones.html', {'form': form, 'pub': pub})


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