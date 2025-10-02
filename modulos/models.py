from django.db import models
from django.contrib.auth.models import User

class ModuloEstudio(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    orden = models.IntegerField(unique=True)
    duracion_estimada = models.IntegerField(help_text="Duración en minutos")
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Módulo {self.orden}: {self.titulo}"

class Leccion(models.Model):
    modulo = models.ForeignKey(ModuloEstudio, on_delete=models.CASCADE, related_name='lecciones')
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    orden = models.IntegerField()
    tipo_contenido = models.CharField(max_length=50, choices=[
        ('teoria', 'Teoría'),
        ('ejemplo', 'Ejemplo'),
        ('ejercicio', 'Ejercicio'),
        ('evaluacion', 'Evaluación')
    ])
    
    class Meta:
        ordering = ['orden']
    
    def __str__(self):
        return f"{self.titulo} - {self.modulo.titulo}"