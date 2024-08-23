from .models import *
from django import forms

class ProcedimientoForm(forms.ModelForm):
    class Meta:
        model = Procedimiento
        fields =[
            'procedimiento',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'sala',
            'usuario',
            'mascota',
        ]
        widgets ={
            'procedimiento': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'hora_inicio': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'hora_fin': forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'sala': forms.Select(attrs={'class':'form-control'}),
            'usuario': forms.Select(attrs={'class':'form-control'}),
            'mascota': forms.Select(attrs={'class':'form-control'}),
        }