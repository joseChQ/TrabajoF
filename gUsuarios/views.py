from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, CreateView, UpdateView
from .forms import CustomUserCreationForm,FormularioLogin
from .models import UserExtra

class Login(FormView):
    template_name = "gUsuarios/login.html"
    form_class = FormularioLogin
    success_url = reverse_lazy('evento')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        login(self.request, form.get_user())
        return super(Login,self).form_valid(form)

class Signup(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'gUsuarios/signup.html'
    def form_valid(self, form):
        if form.is_valid():
            form.save()
        tmp = UserExtra.objects.create(idUser=form.instance)
        tmp.permiso2 = True
        tmp.save()
        return super().form_valid(form)
    