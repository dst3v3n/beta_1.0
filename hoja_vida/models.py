from django.db import models
from .selects import Informacion_Per

# Create your models here.


class Informacion_Person (models.Model):
    Nombre = models.CharField (max_length = 50)
    Apellido = models.CharField (max_length = 50)
    Direccion = models.CharField (max_length = 50)
    Celular = models.IntegerField ()
    Email = models.EmailField (unique=True)
    Fecha = models.DateField ()
    Tipod = models.CharField (max_length = 50 , choices=Informacion_Per.documento())
    N_documento = models.IntegerField ()
    Genero = models.CharField (max_length = 50 , choices=Informacion_Per.genero())
    Edad = models.IntegerField ()
    Civil = models.CharField (max_length = 50 , choices=Informacion_Per.estado_civil())

class Educacion (models.Model):
    Archivo = models.FileField (upload_to='Archivo_Educacion')
    Nombre_Instituto = models.CharField (max_length = 50)
    Ano_graduacion = models.DateField ()
    Tiempo = models.IntegerField ()

class Empresa (models.Model):
    Nombre_empresa = models.CharField (max_length = 50)
    Cargo = models.CharField (max_length = 50)
    Fecha_Inicio = models.DateField ()
    Fecha_Finalizacion = models.DateField ()
    Funciones = models.TextField ()

class Refe_personales (models.Model):
    Nombre_person = models.CharField (max_length = 50)
    Apellido_person = models.CharField (max_length = 50)
    Direccion = models.CharField (max_length = 50)
    N_celular = models.IntegerField ()

class Refe_empresarial (models.Model):
    Nombre_Empresa = models.CharField (max_length = 50)
    Nombre_Jefe = models.CharField (max_length = 50)
    Direccion = models.CharField (max_length = 50)
    N_celular = models.IntegerField ()
