from django.shortcuts import render
from django.http import HttpResponse
from inicio.models import Libro


def inicio(request):

   # return HttpResponse("<h1>Hola soy el proyecto</h1>")
    return render(request, "inicio.html")

def otra(request):

    return render(request, "otra.html")

def agregar_libro(request, titulo, autor):

    libro = Libro(titulo=titulo, autor=autor)
    libro.save()


    return render(request, "agregar_libro.html",{'objeto_guardado': libro})

def listar_libros(request):

    libros = Libro.objects.all()
    
    return render(request, "listar_libros.html", {'listado_de_libros': libros})

