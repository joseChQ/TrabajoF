from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Actividad, Ponente
from gEvento.models import Subevento

class HomePageView(ListView):
    model = Actividad
    template_name = 'actividad.html'
    def get_queryset(self):
        self.subevento = get_object_or_404(Subevento, pk = self.kwargs['pk'])
        return Actividad.objects.filter(idSubevento =self.subevento)
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['subevento'] = self.subevento
        return context

class CrearPonente(CreateView):
    model = Ponente
    template_name = 'ponente_new.html'
    fields = ['nombre','apellido','informacionAcademica','correo']
    def form_valid(self, form):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        form.instance.idActividad = self.actividad
        return super(CrearPonente, self).form_valid(form)

class ListaPonente(ListView):
    model = Ponente
    template_name = 'ponente.html'
    def get_queryset(self):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        return Ponente.objects.filter(idActividad =self.actividad)

    def get_context_data(self, **kwargs):
        context = super(ListaPonente, self).get_context_data(**kwargs)
        context['actividad'] = self.actividad
        return context