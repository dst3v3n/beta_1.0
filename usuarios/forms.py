from django import forms
from .models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class Contact_Form (forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'Fecha': DateInput()
        }