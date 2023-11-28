from django.db import models
from .selects import Informacion_Per
from usuarios.models import Usuario

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
    Usuario = models.ForeignKey (Usuario ,  null=True ,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f" {self.Nombre} {self.Usuario} "

class Educacion (models.Model):
    Archivo = models.FileField (upload_to='Archivo_Educacion')
    Nombre_Instituto = models.CharField (max_length = 50)
    Ano_graduacion = models.DateField ()
    Tiempo = models.IntegerField ()
    Usuario = models.ForeignKey (Usuario , null=True , on_delete=models.CASCADE)

class Empresa (models.Model):
    Nombre_empresa = models.CharField (max_length = 50)
    Cargo = models.CharField (max_length = 50)
    Fecha_Inicio = models.DateField ()
    Fecha_Finalizacion = models.DateField ()
    Funciones = models.TextField ()
    Usuario = models.ForeignKey (Usuario , null=True , on_delete=models.CASCADE)

class Refe_personales (models.Model):
    Nombre_person = models.CharField (max_length = 50)
    Apellido_person = models.CharField (max_length = 50)
    Direccion = models.CharField (max_length = 50)
    N_celular = models.IntegerField ()
    Inforamcion_adi = models.TextField ()
    Usuario = models.ForeignKey (Usuario , null=True , on_delete=models.CASCADE)

class Refe_empresarial (models.Model):
    Nombre_Empresa = models.CharField (max_length = 50)
    Nombre_Jefe = models.CharField (max_length = 50)
    Direccion = models.CharField (max_length = 50)
    N_celular = models.IntegerField ()
    Usuario = models.ForeignKey (Usuario , null=True , on_delete=models.CASCADE)
