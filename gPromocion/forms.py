from django import forms

from .models import Promocion
from gEvento.models import Evento

class Form_Promocion(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = [
            'nombre',
            'actividadesNecesarias',
            'precio',
        ]
        labels = {
            'nombre' : 'Nombre de la promocion',
            'actividadesNecesarias' : 'Activiades Necesarias',
            'precio' : 'Precio',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}), 
            'actividadesNecesarias' : forms.NumberInput(attrs={'class':'form-control'}),
            'precio' : forms.NumberInput(attrs={'class':'form-control','step':'any'}),
        }
        