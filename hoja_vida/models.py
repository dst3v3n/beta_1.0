from django.db import models
from .selects import Informacion_Per

# Create your models here.


class Informacion_Person (models.Model):
    Nombre = models.CharField (max_length = 50)
    Apellido = models.CharField (max_length = 50)
    Direccion = models.CharField (max_length = 50)
    Celular = models.IntegerField ()
    Email = models.EmailField ()
    Fecha = models.DateField ()
    Tipod = models.CharField(max_length = 50 , choices=Informacion_Per.documento())
    N_documento = models.IntegerField ()
    Genero = models.CharField (max_length = 50 , choices=Informacion_Per.genero())
    Edad = models.IntegerField ()
    Civil = models.CharField (max_length = 50 , choices=Informacion_Per.estado_civil())
