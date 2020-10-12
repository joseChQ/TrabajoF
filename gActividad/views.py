from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView
from .models import Actividad, Ponente
from gEvento.models import Subevento

from .forms import Form_Actividad

class ActividadI(ListView):
    model = Ponente
    template_name = 'actividad_detail.html'
    def get_queryset(self):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        return Ponente.objects.filter(idActividad =self.actividad)

    def get_context_data(self, **kwargs):
        context = super(ActividadI, self).get_context_data(**kwargs)
        context['actividad'] = self.actividad
        return context

class CrearPonente(CreateView):
    model = Ponente
    template_name = 'ponente_new.html'
    fields = ['nombre','apellido','informacionAcademica','correo']
    def form_valid(self, form):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        form.instance.idActividad = self.actividad
        return super(CrearPonente, self).form_valid(form)

class CrearActividad(CreateView):
    form_class = Form_Actividad
    template_name = 'actividad_new.html'
    def form_valid(self, form):
        self.subevento = get_object_or_404(Subevento, pk = self.kwargs['pk'])
        form.instance.idSubevento = self.subevento
        return super(CrearActividad, self).form_valid(form)