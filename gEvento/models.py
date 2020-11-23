from django.db import models
from django.urls import reverse
# Requisito: R-006
# Modelo Relacional: MR-011
class Evento(models.Model):
    nombre = models.CharField(max_length = 30)
    detalle = models.CharField(max_length = 50)
    fechaInicio = models.DateField()
    fechaClausura = models.DateField()
    ubicacion = models.CharField(max_length = 30)
    def __str__(self):
        return self.nombre

# Requisito: R-008
# Modelo Relacional: MR-002
class Subevento(models.Model):
    idEvento = models.ForeignKey(Evento, on_delete = models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length = 30)
    fechaInicio = models.DateField()
    fechaClausura = models.DateField()
    def get_absolute_url(self):
        return reverse('eventoDetail', args=[str(self.idEvento.id)])
    def __str__(self):
        return self.nombre

