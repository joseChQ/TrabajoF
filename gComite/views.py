from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import RedirectView
from .models import Comite, Personal
from gEvento.models import Subevento, Evento
from gActividad.models import Actividad
from django.urls import reverse_lazy
from .forms import Form_Comite, Form_Personal
from django.contrib.auth.models import User
# Requisito: R-069
class ComiteI(ListView):
    model = Comite
    template_name = 'comite.html'
    def get_queryset(self):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        tmp = Comite.objects.filter(idEvento=self.evento)
        return tmp.exclude(visibilidad=False)

    def get_context_data(self, **kwargs):
        context = super(ComiteI, self).get_context_data(**kwargs)
        context['evento'] = self.evento
        return context

# Requisito: R-069
class CrearComite(CreateView):
    form_class = Form_Comite
    template_name = 'comite_new.html'
    success_url =""
    def form_valid(self, form):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        form.instance.idEvento = self.evento
        self.success_url = reverse_lazy('comite', args=[str(self.evento.id)])
        return super(CrearComite, self).form_valid(form)

# Requisito: R-069
class ComiteD(ListView):
    model = Personal
    template_name = 'comite_detail.html'
    def get_queryset(self):
        self.comite = get_object_or_404(Comite, pk = self.kwargs['pk'])
        return Personal.objects.filter(comites=self.comite)

    def get_context_data(self, **kwargs):
        context = super(ComiteD, self).get_context_data(**kwargs)
        context['comite'] = self.comite
        return context

# Requisito: R-068
class CrearPersonal(CreateView):
    form_class = Form_Personal
    template_name = 'personal_new.html'
    success_url =""
    def form_valid(self, form):
        self.comite = get_object_or_404(Comite, pk = self.kwargs['pk'])
        if form.is_valid():
            form.save()
        form.instance.comites.add(self.comite)
        self.success_url = reverse_lazy('comiteDetail', args=[str(self.comite.id)])
        return super().form_valid(form)

# Requisito: R-072
class UpdateComite(UpdateView):
    model = Comite
    fields = [
            'nombre',
            'url',
            'descripcion',
        ]
    template_name = 'comite_form.html'
    success_url = ''
    def form_valid(self, form):
        self.comite = get_object_or_404(Comite, pk = self.kwargs['pk'])
        self.success_url = reverse_lazy('comite', args=[str(self.comite.idEvento.id)])
        return super(UpdateComite, self).form_valid(form)

# Requisito: R-072
class EliminarRedirect(RedirectView):
    pattern_name = 'comite'
    def get_redirect_url(self, *args, **kwargs):
        self.comite = get_object_or_404(Comite, pk = self.kwargs['pk'])
        self.comite.visibilidad = False
        self.comite.save()
        return reverse_lazy('comite', args=[str(self.comite.idEvento.id)])