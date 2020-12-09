from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import RedirectView
from .models import Ambiente
from django.urls import reverse_lazy
from .forms import Form_Ambiente
from django.contrib.auth.models import User
# Requisito: R-020
class HomePageView(ListView):
    model = Ambiente
    template_name = 'ambiente.html'
    def get_queryset(self):
        tmp = Ambiente.objects.all()
        return tmp.exclude(visibilidad=False)

# Requisito: R-020
class CrearAmbiente(CreateView):
    form_class = Form_Ambiente
    template_name = 'ambiente_new.html'
    success_url = reverse_lazy('ambiente')

# Requisito: R-018
class UpdateAmbiente(UpdateView):
    model = Ambiente
    fields = ['nombre','descripcion',
            'aforo',
            'puertasEscape',]
    template_name = 'ambiente_form.html'
    success_url = reverse_lazy('ambiente')
# Requisito: R-018
class EliminarRedirect(RedirectView):
    pattern_name = 'ambiente'
    def get_redirect_url(self, *args, **kwargs):
        self.ambiente = get_object_or_404(Ambiente, pk = self.kwargs['pk'])
        self.ambiente.visibilidad = False
        self.ambiente.save()
        return reverse_lazy('ambiente')