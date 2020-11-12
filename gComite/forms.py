from django import forms

from .models import Comite, Personal
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

class Form_Personal(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            'nombre',
            'apellido',
            'DNI',
            'telefono',
            'correoElectronico',
        ]
        labels = {
            'nombre' : 'Nombre',
            'apellido' : 'Apellido',
            'DNI' : 'DNI',
            'telefono' : 'Telefono',
            'correoElectronico' : 'Correo Electronico',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'placeholder':'nombre ejemplo','class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'placeholder':'apellido ejemplo','class':'form-control'}),
            'DNI' : forms.TextInput(attrs={'placeholder':'########','class':'form-control'}),
        }