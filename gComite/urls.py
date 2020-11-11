from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.ComiteI.as_view() , name ='comite'),
    path('Crear/<int:pk>/', views.CrearComite.as_view() , name='crearComite'),
]