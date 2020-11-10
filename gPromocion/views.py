from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView
from django.views.generic.base import RedirectView
from .models import Promocion
from gEvento.models import Subevento, Evento
from gActividad.models import Actividad
from django.urls import reverse_lazy
from .forms import Form_Promocion

class PromocionI(ListView):
    model = Promocion
    template_name = 'promocion.html'
    def get_queryset(self):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        return Promocion.objects.filter(idEvento=self.evento)

    def get_context_data(self, **kwargs):
        context = super(PromocionI, self).get_context_data(**kwargs)
        context['evento'] = self.evento
        return context

class CrearPromocion(CreateView):
    form_class = Form_Promocion
    template_name = 'promocion_new.html'
    success_url =""
    def form_valid(self, form):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        form.instance.idEvento = self.evento
        self.success_url = reverse_lazy('promocion', args=[str(self.evento.id)])
        return super(CrearPromocion, self).form_valid(form)

class PromocionD(ListView):
    model = Actividad
    template_name = 'promocion_detail.html'
    def get_queryset(self):
        self.promocion = get_object_or_404(Promocion, pk = self.kwargs['pk'])
        return Actividad.objects.filter(promocion =self.promocion)

    def get_context_data(self, **kwargs):
        context = super(PromocionD, self).get_context_data(**kwargs)
        context['promocion'] = self.promocion
        return context

class AsignarP(ListView):
    model = Actividad
    template_name = 'promocionA.html'
    def get_queryset(self):
        self.promocion = get_object_or_404(Promocion, pk = self.kwargs['pk'])
        tmp = Actividad.objects.all()
        return tmp.exclude(promocion=self.promocion)

    def get_context_data(self, **kwargs):
        context = super(AsignarP, self).get_context_data(**kwargs)
        context['promocion'] = self.promocion
        return context

class AsignarRedirect(RedirectView):
    pattern_name = 'promocionDetail'
    def get_redirect_url(self, *args, **kwargs):
        self.actividad = get_object_or_404(Actividad, pk = self.kwargs['pk'])
        self.promocion = get_object_or_404(Promocion, pk = self.kwargs['pk1'])
        self.promocion.actividadesP.add(self.actividad)
        return reverse_lazy('promocionDetail', args=[str(self.promocion.id)])