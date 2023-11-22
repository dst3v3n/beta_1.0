from django import forms
from usuarios.models import Usuario

class FormularioAdmin(forms.ModelForm):
    class Meta:
        model=Usuario
        fields='__all__'
