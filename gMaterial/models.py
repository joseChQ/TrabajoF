from django.db import models
from django.urls import reverse
from gEvento.models import Evento
# Requisito: R-034
# Modelo Relacional: MR-010
class Material(models.Model):
    nombre = models.CharField(max_length = 30)
    stock = models.IntegerField()
    costo = models.FloatField()
    visibilidad = models.BooleanField(default=True)
    def get_absolute_url(self):
        return reverse('material')
    def __str__(self):
        return self.nombre

class RegistroMaterial(models.Model):
    MaterialID = models.ForeignKey(Evento, on_delete = models.CASCADE, blank=True, null=True)
    
