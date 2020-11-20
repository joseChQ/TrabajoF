from django import forms

from gEvento.models import Subevento
from .models import Actividad, Ponente
class Form_Actividad(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = [
            'nombre',
            'fechaInicio',
            'fechaClausura',
            'horaInicio',
            'horaFin',
        ]
        labels = {
            'nombre' : 'Nombre de la Actividad',
            'horaInicio' : 'Hora de Inicio',
            'horaFin' : 'Hora de Fin',
            'fechaInicio' : 'Fecha de Inicio',
            'fechaClausura' : 'Fecha de Clausura',
        }
        widgets = {
            # 'nombre' : forms.TextInput(attrs={'placeholder':'Actividad ejemplo'}),
            # 'horaInicio': forms.TextInput(attrs={'type':'time'}),
            # 'horaFin': forms.TextInput(attrs={'type':'time'}),
            # 'fechaInicio': forms.TextInput(attrs={'type':'date'}),
            # 'fechaClausura': forms.TextInput(attrs={'type':'date'}),

            'nombre' : forms.TextInput(attrs={'placeholder':'Actividad ejemplo','class':'form-control'}),
            'horaInicio': forms.TextInput(attrs={'type':'time','class':'form-control'}),
            'horaFin': forms.TextInput(attrs={'type':'time','class':'form-control'}),
            'fechaInicio': forms.TextInput(attrs={'type':'date','class':'form-control'}),
            'fechaClausura': forms.TextInput(attrs={'type':'date','class':'form-control'}),
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
        if horaInicio <= horaFin or fechaInicio1 != fechaClausura1:
            return horaFin
        else:
            raise forms.ValidationError("Hora de fin invalida")


class Form_Ponente(forms.ModelForm):
    class Meta:
        model = Ponente
        fields = [
            'nombre',
            'apellido',
            'informacionAcademica',
            'correo',
        ]
        labels = {
            'nombre' : 'Nombre del Ponente',
            'apellido' : 'Apellido del Ponente',
            'informacionAcademica' : 'Informacion',
            'correo' : 'Correo electronico',
        }
        widgets = {
            'nombre' : forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'apellido': forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'informacionAcademica': forms.TextInput(attrs={'type':'text','class':'form-control'}),
            'correo': forms.TextInput(attrs={'type':'email','class':'form-control'}),
        }