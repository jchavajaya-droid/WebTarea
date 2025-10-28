from django.urls import path
from . import views

urlpatterns = [
    # Estudiantes
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/ver/<int:id>/', views.ver_estudiante, name='ver_estudiante'),

    # Publicaciones
    path('publicaciones/', views.publicaciones, name='publicaciones'),
    path('publicaciones/crear/', views.crear_publicaciones, name='crear_publicidad'),  # <-- aquí arreglamos el nombre
    path('publicaciones/pendientes/', views.lista_publicaciones_pendientes, name='lista_publicaciones_pendientes'),
    path('publicaciones/autorizar/<int:pub_id>/', views.autorizar_publicaciones, name='autorizar_publicaciones'),

    # Administradores
    path('administradores/', views.lista_administradores, name='lista_administradores'),
    path('administradores/agregar/', views.agregar_administrador, name='agregar_administrador'),
    path('administradores/editar/<int:id>/', views.editar_administrador, name='editar_administrador'),
    path('administradores/ver/<int:id>/', views.ver_administrador, name='ver_administrador'),

    # Registro
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),

    # Inicio
    path('', views.inicio, name='inicio'),
]

