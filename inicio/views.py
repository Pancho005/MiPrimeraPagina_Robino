from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Libro, Autor, Genero
from inicio.forms import AgregarLibro, AgregarAutor, AgregarGenero, BuscarLibro
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):

   # return HttpResponse("<h1>Hola soy el proyecto</h1>")
    return render(request, "inicio.html")

def otra(request):

    return render(request, "otra.html")

@login_required
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

    formulario = BuscarLibro(request.GET)
    if formulario.is_valid():
        titulo_a_buscar = formulario.cleaned_data.get("titulo")
        listado_de_libros = Libro.objects.filter(titulo__icontains= titulo_a_buscar)

    libros = Libro.objects.all()
    
    return render(request, "listar_libros.html", {'listado_de_libros': listado_de_libros, "formulario" : formulario})

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

def ver_libro(request, libro_id):

    libro = Libro.objects.get(id=libro_id)
    
    return render(request, "ver_libro.html", {"libro": libro})


class ActualizarLibro(UpdateView):

    model = Libro
    template_name = "actualizar_libro.html"
    fields = "__all__"
    success_url = reverse_lazy("listar")

class EliminarLibro(DeleteView):
    model = Libro
    template_name = "eliminar_libro.html"
    success_url = reverse_lazy("listar")
