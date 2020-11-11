from django import forms

from .models import Comite
from gEvento.models import Evento

class Form_Comite(forms.ModelForm):
    class Meta:
        model = Comite
        fields = [
            'nombre',
            'url',
            'descripcion',
        ]
        labels = {
            'nombre' : 'Nombre del Comite',
            'url' : 'Url',
            'Descripcion' : 'Descripcion',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'placeholder':'compite ejemplo','class':'form-control'}),
            'url' : forms.TextInput(attrs={'placeholder':'no es obligatorio','class':'form-control'}), 
        }
        