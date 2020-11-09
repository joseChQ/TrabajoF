from django.db import models
class Ambiente(models.Model):
    descripcion = models.CharField(max_length = 40)
    aforo = models.IntegerField()
    puertasEscape = models.IntegerField()
    # Eliminar un ambiente
    visibilidad = models.BooleanField(default=True)
    
    def __str__(self):
        return self.id + ': ' + self.descripcion