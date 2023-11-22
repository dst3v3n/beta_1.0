from django.db import models

class Admin (models.Model):
    Nombre = models.CharField (max_length=50 , blank=False , null=False)
    Apellido = models.CharField (max_length=50 , blank=False , null=False)
    Email = models.CharField (max_length=50 , blank=False , null=False , unique=True)
    Password = models.CharField (max_length=50 , blank=False , null=False)

    def __str__(self) -> str:
        return f"{self.Nombre} {self.Apellido}"