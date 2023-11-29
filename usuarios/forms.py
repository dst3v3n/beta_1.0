from django import forms
from .models import Usuario

class PassInput(forms.PasswordInput):
    input_type = 'password'

class FormularioUsario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'Password': PassInput(attrs={'placeholder': 'Ingrese su contraseña, con un mínimo de 8 caracteres.',
                                         'id' : 'passw',
                                         'class' : 'pass'
                                         })
        }
