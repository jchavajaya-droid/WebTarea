from django.urls import path
from . import views

urlpatterns = [
    # Estudiantes
    path('', views.inicio, name='inicio'),
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/agregar/', views.agregar_estudiante, name='agregar_estudiante'),
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/ver/<int:id>/', views.ver_estudiante, name='ver_estudiante'),

    # Administradores
    path('administradores/', views.lista_administradores, name='lista_administradores'),
    path('administradores/agregar/', views.agregar_administrador, name='agregar_administrador'),
    path('administradores/editar/<int:id>/', views.editar_administrador, name='editar_administrador'),
    path('administradores/ver/<int:id>/', views.ver_administrador, name='ver_administrador'),

    # Usuarios
    path('registrar/', views.registrar_usuario, name='registrar_usuario'),

    # Publicaciones
    path('publicaciones/nueva/', views.crear_o_editar_publicacion, name='crear_publicacion'),
    path('publicaciones/editar/<int:pub_id>/', views.crear_o_editar_publicacion, name='editar_publicacion'),
    path('publicaciones/administrar/', views.administrar_publicaciones, name='administrar_publicaciones'),
    path('publicaciones/', views.publicaciones, name='publicaciones'),
]
