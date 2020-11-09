from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.base import RedirectView
from gMaterial.models import Material
from django.urls import reverse_lazy
from .forms import Form_Material

class HomePageView(ListView):
    model = Material
    template_name = 'material.html'

class CrearMaterial(CreateView):
    form_class = Form_Material
    template_name = 'material_new.html'
    success_url = reverse_lazy('material')