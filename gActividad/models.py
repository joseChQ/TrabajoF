from django.db import models
from gEvento.models import Subevento
class Actividad(models.Model):
    idSubevento = models.ForeignKey(Subevento, on_delete = models.CASCADE)
    horaInicio = models.DateTimeField()
    horaFin = models.DateTimeField()
    fechaInicio = models.DateField()
    fechaClausura = models.DateField()

class Ponente(models.Model):
    idActividad = models.ForeignKey(Actividad, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    informacionAcademica = models.CharField(max_length = 30)
    correo = models.EmailField(max_length = 50)
