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
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'stock' : forms.NumberInput(attrs={'class':'form-control'}),
            'costo' : forms.NumberInput(attrs={'class':'form-control', 'step':'any'}),
        }
    