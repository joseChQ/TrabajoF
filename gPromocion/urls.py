from django.urls import path
from . import views
#app_name = 'actividadapp'
urlpatterns = [
    path('<int:pk>/', views.PromocionI.as_view() , name ='promocion'),
    path('Crear/<int:pk>/', views.CrearPromocion.as_view() , name='crearPromocion'),
    path('Detail/<int:pk>/', views.PromocionD.as_view() , name='promocionDetail'),
    path('Asignar/<int:pk>/', views.AsignarP.as_view() , name='asignarP'),
    path('Redirect/<int:pk>/<int:pk1>/', views.AsignarRedirect.as_view() , name ='RedirectP'),
]