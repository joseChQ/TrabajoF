from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, FormView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.

# Base de datos
from .models import Evento
from .models import Subevento
from gUsuarios.models import UserExtra
# Tipos de formularios
from .forms import Form_Evento, Form_Subevento
from gActividad.models import Actividad
from gPromocion.models import Promocion


# from .models import *
# Requisito: R-006
class HomePageView(ListView):
    model = Evento
    template_name = 'evento.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        Usercurrent = get_object_or_404(User,pk=self.request.user.id)
        userX = get_object_or_404(UserExtra,idUser = Usercurrent)
        context['permiso1'] = userX.permiso1
        return context

# Requisito: R-006
class EventoI(ListView):
    model = Subevento
    template_name = 'evento_detail.html'
    #UserCurrent = User.objects.filter(id=1)
    def get_queryset(self):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        return Subevento.objects.filter(idEvento =self.evento)

    def get_context_data(self, **kwargs):
        context = super(EventoI, self).get_context_data(**kwargs)
        promociones = Promocion.objects.filter(idEvento = self.evento)
        Usercurrent = get_object_or_404(User,pk=self.request.user.id)
        userX = get_object_or_404(UserExtra,idUser = Usercurrent)
        context['evento'] = self.evento
        context['promociones'] = promociones
        context['permiso1'] = userX.permiso1
        return context

# Requisito: R-006
class CrearEvento(CreateView):
    template_name = 'evento_new.html'
    form_class = Form_Evento
    success_url = reverse_lazy('evento')


# Requisito: R-008
class CrearSubevento(CreateView):
    form_class = Form_Subevento
    template_name = 'subevento_new.html'
    def form_valid(self, form):
        self.evento = get_object_or_404(Evento, pk = self.kwargs['pk'])
        form.instance.idEvento = self.evento
        return super(CrearSubevento, self).form_valid(form)

# Requisito: R-008
class SubeventoI(ListView):
    model = Actividad
    template_name = 'subevento_detail.html'
    def get_queryset(self):
        self.subevento = get_object_or_404(Subevento, pk = self.kwargs['pk'])
        return Actividad.objects.filter(idSubevento =self.subevento)
    def get_context_data(self, **kwargs):
        context = super(SubeventoI, self).get_context_data(**kwargs)
        Usercurrent = get_object_or_404(User,pk=self.request.user.id)
        userX = get_object_or_404(UserExtra,idUser = Usercurrent)
        context['permiso1'] = userX.permiso1
        context['subevento'] = self.subevento
        return context    