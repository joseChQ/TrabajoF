from django import forms

from .models import Ambiente

class Form_Ambiente(forms.ModelForm):
    class Meta:
        model = Ambiente
        fields = [
            'nombre',
            'descripcion',
            'aforo',
            'puertasEscape',
        ]
        labels = {
            'nombre' : 'Nombre del Ambiente',
            'descripcion' : 'Descripcion',
            'aforo' : 'Aforo',
            'puertasEscape' : 'Cantidad de puertas',
        }
        widgets = {      
            'descripcion' : forms.TextInput(attrs={'placeholder':'descripcion ejemplo','class':'form-control'}),
        }