from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView
# Create your views here.

# Base de datos
from .models import Evento
from .models import Subevento

# Tipos de formularios
from .forms import Formulario_Evento

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

class CrearEvento(CreateView):
    model = Evento
    template_name = 'evento_new.html'
    fields = ['nombre','fechaInicio','fechaClausura','ubicacion']


def crear_evento(request):
        if request.method =='POST':
            form_Evento = Formulario_Evento(request.post)
            
            if form_Evento.is_valid():
                infForm = form_Evento.cleaned_data()
                
        else:
            form_Evento = Formulario_Evento()
        
        return render(request,'evento_new.html', {"form":form_Evento})