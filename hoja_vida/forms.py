from django import forms
from . models import Informacion_Person

class text (forms.TextInput):
    input_type = 'text'

class Form_Info_Person (forms.ModelForm):
    class Meta:
        model = Informacion_Person
        fields = '__all__'
        widgets = {
            'Nombre': text(attrs={'class': 'inp'}),
            'Apellido': text(attrs={'class': 'inp'}),
        }
