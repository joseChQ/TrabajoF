from django.contrib import admin

# Register your models here.
from gEvento.models import Evento , Subevento
admin.site.register(Evento)
admin.site.register(Subevento)