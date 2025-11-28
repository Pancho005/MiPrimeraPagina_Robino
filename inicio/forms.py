from django import forms
from .models import Autor, Genero, Libro

class AgregarAutor(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre', 'nacionalidad']


class AgregarGenero(forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']


class AgregarLibro(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor']

class BuscarLibro(forms.Form):
    titulo = forms.CharField(max_length=100, required=False)





"""class AgregarAutor(forms.Form):
    nombre = forms.CharField(max_length=100)
    nacionalidad = forms.CharField(max_length=100)



class AgregarGenero(forms.Form):
    nombre = forms.CharField(max_length=100)



class AgregarLibro(forms.Form):
    titulo = forms.CharField(max_length=100)
    autor = forms.CharField(max_length=100)
   """