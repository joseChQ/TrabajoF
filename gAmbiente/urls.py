from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='ambiente'),
    path('Crear', views.CrearAmbiente.as_view(), name='crearAmbiente'),
]
