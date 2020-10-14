from django import forms

from .models import Evento ,Subevento

class Form_Evento(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'nombre',
            'detalle',
            'fechaInicio',
            'fechaClausura',
            'ubicacion',
        ]
        labels = {
            'nombre' : 'Nombre del Evento',
            'detalle' : 'Detalle del Evento',
            'fechaInicio' : 'Fecha de Inicio',
            'fechaClausura' : 'Fecha de Clausura',
            'ubicacion' : 'Ubicacion',
        }
        widgets = {
            # 'nombre' : forms.TextInput(attrs={'placeholder':'evento ejemplo'}),
            # 'detalle': forms.TextInput(),
            # 'fechaInicio': forms.TextInput(attrs={'type':'date'}),
            # 'fechaClausura': forms.TextInput(attrs={'type':'date'}),
            # 'ubicacion': forms.TextInput(),

            'nombre' : forms.TextInput(attrs={'placeholder':'evento ejemplo','class':'form-control'}),
            'detalle': forms.TextInput(attrs={'class':'form-control'}),
            'fechaInicio': forms.TextInput(attrs={'type':'date','class':'form-control'}),
            'fechaClausura': forms.TextInput(attrs={'type':'date','class':'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class':'form-control'}),   
        }

    def clean_fechaClausura(self, *args, **kwargs):
        fechaInicio = self.cleaned_data.get("fechaInicio")
        fechaClausura = self.cleaned_data.get("fechaClausura")
        if fechaInicio <= fechaClausura:
            return fechaClausura
        else:
            raise forms.ValidationError("Fecha de clausura invalida")

class Form_Subevento(forms.ModelForm):
    class Meta:
        model = Subevento
        fields = [
            'nombre',
            'fechaInicio',
            'fechaClausura',
        ]
        labels = {
            'nombre' : 'Nombre del Subevento',
            'fechaInicio' : 'Fecha de Inicio',
            'fechaClausura' : 'Fecha de Clausura',
        }
        widgets = {
            # 'nombre' : forms.TextInput(attrs={'placeholder':'subevento ejemplo'}),
            # 'fechaInicio': forms.TextInput(attrs={'type':'date'}),
            # 'fechaClausura': forms.TextInput(attrs={'type':'date'}),

            'nombre' : forms.TextInput(attrs={'placeholder':'subevento ejemplo','class':'form-control'}),
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
        