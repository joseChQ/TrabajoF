from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='material'),
    path('Crear', views.CrearMaterial.as_view(), name='crearMaterial'),
]
