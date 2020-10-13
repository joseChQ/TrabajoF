from django.urls import path
from . import views
#app_name = 'actividadapp'
urlpatterns = [
    path('<int:pk>/', views.ActividadI.as_view() , name ='actividadDetail'),
    path('Ponente/crear/<int:pk>/', views.CrearPonente.as_view() , name ='crearPonente'),
    path('Actividad/crear/<int:pk>/', views.CrearActividad.as_view() , name ='crearActividad'),
    path('ListaPonente/<int:pk>/', views.ListaPonente.as_view() , name ='listaPonente'),
    path('Redirect/<int:pk>/<int:pk1>/', views.AsignarRedirect.as_view() , name ='asignarRedirect'),
]