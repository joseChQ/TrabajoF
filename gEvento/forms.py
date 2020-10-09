from django import forms

class Formulario_Evento(forms.Form):
    nombre = forms.CharField()
    fecha_Inicio = forms.DateField()
    fecha_Clausura = forms.DateField()