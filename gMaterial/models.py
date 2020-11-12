from django.db import models
from django.urls import reverse
class Material(models.Model):
    nombre = models.CharField(max_length = 30)
    stock = models.IntegerField()
    costo = models.FloatField()
    visibilidad = models.BooleanField(default=True)
    def get_absolute_url(self):
        return reverse('material')
    def __str__(self):
        return self.nombre
    