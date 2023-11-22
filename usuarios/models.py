from django.db import models
from HumanTalentSena.static.python.encriptar import encriptar

# Create your models here.
class Usuario (models.Model):
    Nombre = models.CharField (max_length=50 , blank=False , null=False)
    Apellido = models.CharField (max_length=50 , blank=False , null=False)
    Email = models.CharField (max_length=50 , blank=False , null=False , unique=True)
    Password = models.CharField (max_length=50 , blank=False , null=False)

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"
    
    def encriptacion (self , password:str):
        self.Password = password
        return self.Password


class User (models.Model):
    Nombre = models.CharField (max_length=50)
    Apellido = models.CharField (max_length=50)
    Fecha = models.DateField ()
    # Documento = models.IntegerField ()

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"