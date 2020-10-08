from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='evento'),
    path('listaSubevento/<int:pk>/', views.VistaSubevento.as_view() , name='subevento')
]