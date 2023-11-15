from django.db import models

# Create your models here.
class Usuario (models.Model):
    Nombre = models.CharField (max_length=50)
    Apellido = models.CharField (max_length=50)
    Email = models.CharField (max_length=50)
    Password = models.CharField (max_length=50)

    def __str__(self):
        return self.Nombre