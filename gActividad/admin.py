from django.contrib import admin

# Register your models here.
from gActividad.models import Actividad , Ponente
admin.site.register(Actividad)
admin.site.register(Ponente)