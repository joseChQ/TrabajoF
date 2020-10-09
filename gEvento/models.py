from django.db import models
from django.urls import reverse
class Evento(models.Model):
    nombre = models.CharField(max_length = 30)
    fechaInicio = models.DateField()
    fechaClausura = models.DateField()
    ubicacion = models.CharField(max_length = 30)
    def get_absolute_url(self):
        return reverse('evento')

class Subevento(models.Model):
    idEvento = models.ForeignKey(Evento, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 30)
    fechaInicio = models.DateField()
    fechaClausura = models.DateField()