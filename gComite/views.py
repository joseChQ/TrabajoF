from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.base import RedirectView
from .models import Comite
from gEvento.models import Subevento, Evento
from gActividad.models import Actividad
from django.urls import reverse_lazy
from .forms import Form_Comite

class ComiteI(ListView):
    model = Comite
    template_name = 'comite.html'
    def get_queryset(self):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        return Comite.objects.filter(idEvento=self.evento)

    def get_context_data(self, **kwargs):
        context = super(ComiteI, self).get_context_data(**kwargs)
        context['evento'] = self.evento
        return context

class CrearComite(CreateView):
    form_class = Form_Comite
    template_name = 'comite_new.html'
    success_url =""
    def form_valid(self, form):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        form.instance.idEvento = self.evento
        self.success_url = reverse_lazy('comite', args=[str(self.evento.id)])
        return super(CrearComite, self).form_valid(form)