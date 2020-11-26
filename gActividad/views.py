from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.base import RedirectView
from .models import Actividad, Ponente
from gEvento.models import Subevento
from django.urls import reverse_lazy
from .forms import Form_Actividad, Form_Ponente

# Requisito: R-027
class ActividadI(ListView):
    model = Ponente
    template_name = 'actividad_detail.html'
    def get_queryset(self):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        return Ponente.objects.filter(actividades=self.actividad)

    def get_context_data(self, **kwargs):
        context = super(ActividadI, self).get_context_data(**kwargs)
        context['actividad'] = self.actividad
        return context

# Requisito: R-029
class CrearPonente(CreateView):
    form_class = Form_Ponente
    template_name = 'ponente_new.html'
    success_url =""
    def form_valid(self, form):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        if form.is_valid():
            form.save()
        form.instance.actividades.add(self.actividad)
        self.success_url = reverse_lazy('actividadDetail', args=[str(self.actividad.id)])
        return super().form_valid(form)

# Requisito: R-027
class CrearActividad(CreateView):
    form_class = Form_Actividad
    template_name = 'actividad_new.html'
    def form_valid(self, form):
        self.subevento = get_object_or_404(Subevento, pk = self.kwargs['pk'])
        form.instance.idSubevento = self.subevento
        return super(CrearActividad, self).form_valid(form)

# Requisito: R-029
class ListaPonente(ListView):
    model = Ponente
    template_name = 'lista_ponente.html'
    def get_queryset(self):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        tmp = Ponente.objects.all()
        return tmp.exclude(actividades=self.actividad)

    def get_context_data(self, **kwargs):
        context = super(ListaPonente, self).get_context_data(**kwargs)
        context['actividad'] = self.actividad
        return context

# Requisito: R-028
class AsignarRedirect(RedirectView):
    pattern_name = 'actividadDetail'
    def get_redirect_url(self, *args, **kwargs):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        self.ponente = get_object_or_404(Ponente, pk = self.kwargs['pk1'])
        self.ponente.actividades.add(self.actividad)
        #return super().get_redirect_url(args=[str(self.actividad.id)], **kwargs)
        return reverse_lazy('actividadDetail', args=[str(self.actividad.id)])

    