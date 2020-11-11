from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='ambiente'),
    path('Crear', views.CrearAmbiente.as_view(), name='crearAmbiente'),
    path('Eliminar/<int:pk>/', views.EliminarRedirect.as_view(), name='eliminarAmbiente'),
    path('Update/<int:pk>/', views.UpdateAmbiente.as_view(), name='updateAmbiente'),
]
