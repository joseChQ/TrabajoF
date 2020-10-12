from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='evento'),
    path('Evento/<int:pk>/', views.EventoI.as_view() , name='eventoDetail'),
    path('crearEvento/', views.CrearEvento.as_view() , name='crearEvento'),
    path('crearSubevento/<int:pk>/', views.CrearSubevento.as_view() , name ='crearSubevento'),
    path('Subvento/<int:pk>/', views.SubeventoI.as_view() , name='subeventoDetail'),
]
