from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)

    def __str__(self):
        return f'Libro ({self.id}): {self.titulo} - {self.autor}'
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, blank=True)

    
    def __str__(self):
        return f'Autor ({self.id}): {self.nombre} - {self.nacionalidad}'


class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return f'Genero ({self.id}): {self.nombre}'
