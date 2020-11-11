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