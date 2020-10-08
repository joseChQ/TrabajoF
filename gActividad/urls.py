from django.urls import path
from . import views
#app_name = 'actividadapp'
urlpatterns = [
    path('<int:pk>/', views.HomePageView.as_view() , name ='actividad'),
    path('Ponente/crear/<int:pk>/', views.CrearPonente.as_view() , name ='crearPonente'),
    path('Ponente/lista/<int:pk>/', views.ListaPonente.as_view() , name ='listaPonente')
]