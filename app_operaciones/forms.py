from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

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

class RegistroUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields =[
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }

    def save(self, commit=True):
        user = super(RegistroUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
    
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
                               
                            