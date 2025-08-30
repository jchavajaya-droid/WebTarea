from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html')

def acerca(request):
    return render(request, 'acerca.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def administradores(request):
    return render(request, 'administradores.html')
