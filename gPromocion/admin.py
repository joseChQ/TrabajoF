from django.contrib import admin

# Register your models here.
from gPromocion.models import Promocion, ActividadPromocion
admin.site.register(Promocion)
admin.site.register(ActividadPromocion)