from django.db import models
from gActividad.models import Actividad
from gEvento.models import Evento
# Create your models here.
class Comite(models.Model):
    idEvento = models.ForeignKey(Evento, on_delete = models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length = 15)
    url = models.CharField(max_length = 40, blank=True, null=True)
    descripcion = models.CharField(max_length = 45)
    visibilidad = models.BooleanField(default=True)

class Personal(models.Model):
    comites = models.ManyToManyField(
        Comite,
        through='ComitePersonal'
    )
    nombre = models.CharField(max_length = 15)
    apellido = models.CharField(max_length = 15)
    DNI = models.CharField(max_length = 8)
    telefono = models.CharField(max_length = 9)
    correoElectronico = models.EmailField(max_length = 45)

class ComitePersonal(models.Model):
    comite = models.ForeignKey(Comite, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    