from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class UserExtra(models.Model):
    idUser = models.ForeignKey(User, on_delete = models.CASCADE)
    codeQR = models.ImageField(blank = True, null = True)
    permiso1 = models.BooleanField(default=False)
    permiso2 = models.BooleanField(default=False)
    permiso3 = models.BooleanField(default=False)


