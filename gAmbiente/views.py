from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.base import RedirectView
from .models import Ambiente
from django.urls import reverse_lazy
from .forms import Form_Ambiente

class HomePageView(ListView):
    model = Ambiente
    template_name = 'ambiente.html'

class CrearAmbiente(CreateView):
    form_class = Form_Ambiente
    template_name = 'ambiente_new.html'
    success_url = reverse_lazy('ambiente')
