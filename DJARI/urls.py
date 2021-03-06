"""DJARI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gEvento.urls')), # templates ordenados 
    path('gActividad/', include('gActividad.urls')), # templates ordenados
    path('gMaterial/', include('gMaterial.urls')), # templates ordenados
    path('gAmbiente/', include('gAmbiente.urls')), # templates ordenados
    path('gPromocion/', include('gPromocion.urls')), # templates ordenados
    path('gComite/', include('gComite.urls')), # templates ordenados
    path('gUsuarios/',include('gUsuarios.urls')), # templates ordenados
]
