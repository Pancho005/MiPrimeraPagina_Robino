from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Libro, Autor, Genero
from inicio.forms import AgregarLibro, AgregarAutor, AgregarGenero


def inicio(request):

   # return HttpResponse("<h1>Hola soy el proyecto</h1>")
    return render(request, "inicio.html")

def otra(request):

    return render(request, "otra.html")

def agregar_libro(request):
    libro = ''
    if request.method == 'POST':
        formulario = AgregarLibro(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            libro = Libro(titulo=info.get('titulo'), autor=info.get('autor'))
            libro.save()
            
            return redirect("listar")
    else:
        formulario = AgregarLibro()

    return render(request, "agregar_libro.html",{'formulario': formulario})

def listar_libros(request):

    libros = Libro.objects.all()
    
    return render(request, "listar_libros.html", {'listado_de_libros': libros})

def agregar_autor(request):

    autor = ''
    if request.method == 'POST':
        formulario = AgregarAutor(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            autor = Autor(nombre=info.get('nombre'), nacionalidad=info.get('nacionalidad'))
            autor.save()
            formulario.save()
            
            return redirect("listar")
    else:
        formulario = AgregarAutor()

    return render(request, "agregar_autor.html",{'formulario': formulario})

def agregar_genero(request):

    genero = ''
    if request.method == 'POST':
        formulario = AgregarGenero(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data

            genero = Genero(nombre=info.get('nombre'))
            genero.save()
            formulario.save()
            
            return redirect("listar")
    else:
        formulario = AgregarGenero()

    return render(request, "agregar_genero.html",{'formulario': formulario})

    