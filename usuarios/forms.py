from django import forms
from .models import Usuario

class Contact_Form (forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
