from django.db import models

# Create your models here.

class Empresa (models.Model):
    Nombre_emp = models.CharField (max_length=50 , blank=False , null=False)
    NIT = models.CharField (max_length=15 , blank=False , null=False)
    Email = models.CharField (max_length=50 , blank=False , null=False , unique=True)
    Password = models.CharField (max_length=50 , blank=False , null=False)

    def __str__(self):
        return f"{self.Nombre_emp}"
