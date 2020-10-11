from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, FormView
from django.urls import reverse_lazy
# Create your views here.

# Base de datos
from .models import Evento
from .models import Subevento

# Tipos de formularios
from .forms import Form_Evento

# from .models import *

class HomePageView(ListView):
    model = Evento
    template_name = 'evento.html'


class VistaSubevento(ListView):
    model = Subevento
    template_name = 'subevento.html'
    def get_queryset(self):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        return Subevento.objects.filter(idEvento =self.evento)
    def get_context_data(self, **kwargs):
        context = super(VistaSubevento, self).get_context_data(**kwargs)
        context['evento'] = self.evento
        return context

class CrearEvento(FormView):
    template_name = 'evento_new.html'
    form_class = Form_Evento
    success_url = reverse_lazy('evento')
    
    def form_valid(self, form):
       if form.is_valid():
           form.save();  
       return super().form_valid(form)
