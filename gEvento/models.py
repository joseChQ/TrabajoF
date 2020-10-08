from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length = 30)
    fechaInicio = models.DateField()
    fechaClausura = models.DateField()
    ubicacion = models.CharField(max_length = 30)

class Subevento(models.Model):
    idEvento = models.ForeignKey(Evento, on_delete = models.CASCADE)
    nombre = models.CharField(max_length = 30)
    fechaInicio = models.DateField()
    fechaClausura = models.DateField()