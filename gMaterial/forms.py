from django import forms

from .models import Material

class Form_Material(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            'nombre',
            'stock',
            'costo',
        ]
        labels = {
            'nombre' : 'Nombre del material',
            'stock' : 'Stock',
            'costo' : 'Costo',
        }
        widgets = {      
            'nombre' : forms.TextInput(attrs={'placeholder':'material ejemplo','class':'form-control'}),
        }