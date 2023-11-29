from django import forms
from .models import Empresa

class PassInput(forms.PasswordInput):
    input_type = 'password'

class FormularioEmpresa(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'Password': PassInput(attrs={'placeholder': 'Ingrese su contraseña, con un mínimo de 8 caracteres.',
                                         'id' : 'passw',
                                         'class' : 'pass'
                                         })
        }
