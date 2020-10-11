from django import forms

from .models import Evento

class Form_Evento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'nombre',
            'fechaInicio',
            'fechaClausura',
            'ubicacion',
        ]
        labels = {
            'nombre' : 'Nombre del Evento',
            'fechaInicio' : 'Fecha de Inicio',
            'fechaClausura' : 'Fecha de Clausura',
            'ubicacion' : 'Ubicacion',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'placeholder':'evento ejemplo'}),
            'fechaInicio': forms.TextInput(attrs={'type':'date'}),
            'fechaClausura': forms.TextInput(attrs={'type':'date'}),
            'ubicacion': forms.TextInput(),
        }
    