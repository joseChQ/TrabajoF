from django.db import models
# Requisito: R-020
# Modelo Relacional: MR-015
class Ambiente(models.Model):
    nombre = models.CharField(max_length = 40)
    descripcion = models.CharField(max_length = 40)
    aforo = models.IntegerField()
    puertasEscape = models.IntegerField()
    # Eliminar un ambiente
    visibilidad = models.BooleanField(default=True)
    
    def __str__(self):
        return self.id + ': ' + self.descripcion