from django.db import models

# Create your models here.
class Filtro (models.Model):
        rango_salario = models.IntegerField ()
        rango_exp = models.IntegerField()
        tipo_ocupacion = models.CharField (max_length = 50)
        ubicacion_des =  models.CharField (max_length = 50)
        horario_des =  models.CharField (max_length = 50)
        tipo_contr_des =  models.CharField (max_length = 50)
        teletrabajo =  models.CharField (max_length = 50)

class resultados (models.Model):
        codigo_oferta = models.IntegerField()
        num_vacante = models.IntegerField()
        fecha_inicio =  models.DateField ()
        fecha_cierre =  models.DateField ()
        rango_salaria = models.IntegerField()
        experiencia = models.CharField (max_length = 50)
        tipo_contrato = models.CharField (max_length = 50)
        teletrabajo = models.CharField (max_length = 50)
        rango_salario = models.IntegerField ()
        rango_exp = models.IntegerField ()
        tipo_ocupacion = models.CharField (max_length = 50)
        ubicacion = models.CharField (max_length = 50)
        horario_des = models.CharField (max_length = 50)
        tipo_conta_des = models.CharField (max_length = 50)

