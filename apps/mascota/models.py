from django.db import models
from apps.adopcion.models import Persona
# Create your models here.

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)


class Mascota(models.Model):
    persona=models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
    folio = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    vacuna = models.ManyToManyField(Vacuna)
