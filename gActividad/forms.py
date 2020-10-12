from django import forms

from gEvento.models import Subevento
from .models import Actividad
class Form_Actividad(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = [
            'nombre',
            'horaInicio',
            'horaFin',
            'fechaInicio',
            'fechaClausura',
        ]
        labels = {
            'nombre' : 'Nombre del Evento',
            'horaInicio' : 'Hora de Inicio',
            'horaFin' : 'Hora de Fin',
            'fechaInicio' : 'Fecha de Inicio',
            'fechaClausura' : 'Fecha de Clausura',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'placeholder':'Actividad ejemplo'}),
            'horaInicio': forms.TextInput(attrs={'type':'time'}),
            'horaFin': forms.TextInput(attrs={'type':'time'}),
            'fechaInicio': forms.TextInput(attrs={'type':'date'}),
            'fechaClausura': forms.TextInput(attrs={'type':'date'}),
        }

    def clean_fechaClausura(self, *args, **kwargs):
        fechaInicio = self.cleaned_data.get("fechaInicio")
        fechaClausura = self.cleaned_data.get("fechaClausura")
        if fechaInicio <= fechaClausura:
            return fechaClausura
        else:
            raise forms.ValidationError("Fecha de clausura invalida")

    def clean_horaFin(self, *args, **kwargs):
        horaInicio = self.cleaned_data.get("horaInicio")
        horaFin = self.cleaned_data.get("horaFin")
        fechaInicio1 = self.fields["fechaInicio"]
        fechaClausura1 = self.cleaned_data.get("fechaClausura")
        print(horaInicio)
        print(horaFin)
        if horaInicio <= horaFin:
            return horaFin
        else:
            raise forms.ValidationError("Hora de fin invalida")        