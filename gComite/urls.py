from django.urls import path
from . import views
urlpatterns = [
    path('<int:pk>/', views.ComiteI.as_view() , name ='comite'),
    path('Crear/<int:pk>/', views.CrearComite.as_view() , name='crearComite'),
    path('Detail/<int:pk>/', views.ComiteD.as_view() , name='comiteDetail'),
    path('CrearP/<int:pk>/', views.CrearPersonal.as_view() , name='crearPersonal'),
    path('Update/<int:pk>/', views.UpdateComite.as_view(), name='updateComite'),
    path('Eliminar/<int:pk>/', views.EliminarRedirect.as_view(), name='eliminarComite'),

]