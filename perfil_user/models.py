from django.db import models
from usuarios.models import Usuario

class Perfil(models.Model):
    usuario = models.OneToOneField(Usuario)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    trabajo = models.CharField(max_length=100, blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    ubicacion = models.CharField(max_length=100, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    registro = models.DateTimeField(auto_now_add=True)
    redes_sociales = models.URLField(blank=True, null=True)
    fondo = models.ImageField(upload_to='fondos/', blank=True, null=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre_usuario} {self.direccion}"
