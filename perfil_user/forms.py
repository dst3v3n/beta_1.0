from django import forms
from . models import Perfil

class Date (forms.DateInput):
    input_type = 'date'

class Form_Info_Perfil (forms.ModelForm):
    class Meta:
        model = Perfil
        fields = '__all__'
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'perf'}),
            'Apellido': forms.TextInput(attrs={'class': 'perf'}),
            'Direccion': forms.TextInput(attrs={'class': 'perf'}),
            'telefono' : forms.NumberInput (attrs={'class': 'perf'}),
            'cargo': forms.TextInput(attrs={'class': 'perf'}),
            'Fecha_nacimiento' : forms.DateInput (attrs={'class': 'perf'}),
            'redes_sociales': forms.URLInput(attrs={'class': 'perf'}),
            'fondo': forms.FileInput(attrs={'class': 'fondo_per'}),
            'foto_perfil': forms.FileInput(attrs={'class': 'foto_per'}),
        }
