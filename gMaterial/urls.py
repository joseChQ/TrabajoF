from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='material'),
    path('Crear', views.CrearMaterial.as_view(), name='crearMaterial'),
    path('Update/<int:pk>/', views.UpdateMaterial.as_view(), name='updateMaterial'),
    path('Eliminar/<int:pk>/', views.EliminarRedirect.as_view(), name='eliminarMaterial'),
]
