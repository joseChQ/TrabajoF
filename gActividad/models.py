from django.db import models
from gEvento.models import Subevento
from django.urls import reverse
class Actividad(models.Model):
    idSubevento = models.ForeignKey(Subevento, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 30)
    horaInicio = models.TimeField()
    horaFin = models.TimeField()
    fechaInicio = models.DateField()
    fechaClausura = models.DateField()
    def get_absolute_url(self):
        return reverse('subeventoDetail', args=[str(self.idSubevento.id)])
    def __str__(self):
        return self.nombre

class Ponente(models.Model):
    idActividad = models.ForeignKey(Actividad, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    informacionAcademica = models.CharField(max_length = 30)
    correo = models.EmailField(max_length = 50)
    def get_absolute_url(self):
        return reverse('listaPonente', args=[str(self.idActividad.id)])
    def __str__(self):
        return self.nombre