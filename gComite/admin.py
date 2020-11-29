from django.contrib import admin

# Register your models here.
from gComite.models import Comite , Personal, ComitePersonal
admin.site.register(Comite)
admin.site.register(Personal)
admin.site.register(ComitePersonal)