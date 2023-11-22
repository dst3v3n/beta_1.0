from django import forms
from usuarios.models import Usuario

class eliminarUser(forms.ModelForm):
    class Meta:
        model=Usuario
        fields='_all_'
