from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView
# Create your views here.

from .models import Evento
from .models import Subevento

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

