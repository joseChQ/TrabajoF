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
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'placeholder':'opcional','class':'form-control'}), 
            'descripcion' : forms.TextInput(attrs={'class':'form-control'}), 
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
            'nombre' : forms.TextInput(attrs={'placeholder':'nombres','class':'form-control'}),
            'apellido' : forms.TextInput(attrs={'placeholder':'apellidos','class':'form-control'}),
            'DNI' : forms.TextInput(attrs={'placeholder':'########','class':'form-control','maxlength':'2'}),
            'telefono' : forms.TextInput(attrs={'placeholder':'########','class':'form-control','maxlength':'2'}),
            'correoElectronico' : forms.TextInput(attrs={'type':'email','placeholder':'djari..@gmail.com','class':'form-control'}),
        }