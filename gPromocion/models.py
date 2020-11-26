from django.db import models
from gActividad.models import Actividad
from gEvento.models import Evento
# Create your models here.

# Requisito: R-079
# Modelo Relacional: MR-006
class Promocion(models.Model):
    actividadesP = models.ManyToManyField(
        Actividad,
        through='ActividadPromocion'
    )
    idEvento = models.ForeignKey(Evento, on_delete = models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length = 15)
    actividadesNecesarias = models.IntegerField()
    precio = models.FloatField()
    visibilidad = models.BooleanField(default=True) 
    def get_absolute_url(self):
        return reverse('eventoDetail', args=[str(self.idEvento.id)])

    def __str__(self):
        return self.nombre

# Requisito: R-081
class ActividadPromocion(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    def get_absolute_url(self):
        return reverse('eventoDetail', args=[str(self.promocion.idEvento.id)])