from django.shortcuts import render , get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import RedirectView
from gMaterial.models import Material
from django.urls import reverse_lazy
from .forms import Form_Material
from django.contrib.auth.models import User
from gUsuarios.models import UserExtra
# Requisito: R-034
class HomePageView(ListView):
    model = Material
    template_name = 'material.html'
    def get_queryset(self):
        tmp = Material.objects.all()
        return tmp.exclude(visibilidad=False)
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        Usercurrent = get_object_or_404(User,pk=self.request.user.id)
        userX = get_object_or_404(UserExtra,idUser = Usercurrent)
        context['permiso1'] = userX.permiso1
        return context

# Requisito: R-034
class CrearMaterial(CreateView):
    form_class = Form_Material
    template_name = 'material_new.html'
    success_url = reverse_lazy('material')
# Requisito: R-034
class UpdateMaterial(UpdateView):
    model = Material
    fields = ['nombre',
            'stock',
            'costo',]
    template_name = 'material_form.html'
    success_url = reverse_lazy('material')

# Requisito: R-034
class EliminarRedirect(RedirectView):
    pattern_name = 'material'
    def get_redirect_url(self, *args, **kwargs):
        self.material = get_object_or_404(Material, pk = self.kwargs['pk'])
        self.material.visibilidad = False
        self.material.save()
        return reverse_lazy('material')