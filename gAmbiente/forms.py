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
            'descripcion' : 'Descripción',
            'aforo' : 'Aforo',
            'puertasEscape' : 'Cantidad de puertas de escape ',
        }
        widgets = {      
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
            'aforo' : forms.NumberInput(attrs={'class':'form-control'}),
            'puertasEscape' : forms.NumberInput(attrs={'class':'form-control'}),
        }