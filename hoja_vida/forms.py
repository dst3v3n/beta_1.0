from django import forms
from . models import Informacion_Person , Educacion , Empresa , Refe_personales , Refe_empresarial , Informacion_Adicional

class Date (forms.DateInput):
    input_type = 'date'

class Form_Info_Person (forms.ModelForm):
    class Meta:
        model = Informacion_Person
        fields = ['Nombre' , 'Apellido' , 'Direccion' , 'Celular' , 'Email' , 'Fecha' , 'Tipod' , 'N_documento' , 'Genero' , 'Edad' , 'Civil']
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'inp', }),
            'Apellido': forms.TextInput(attrs={'class': 'inp'}),
            'Direccion': forms.TextInput(attrs={'class': 'inp'}),
            'Celular' : forms.NumberInput (attrs={'class': 'inp1'}),
            'Email' : forms.EmailInput (attrs={'class': 'inp'}),
            'Fecha' : Date (attrs={'class': 'inp2'}),
            'Tipod': forms.Select(attrs={'class': 'inp2'}),
            'N_documento' : forms.NumberInput (attrs={'class': 'inp1'}),
            'Genero': forms.Select(attrs={'class': 'inp2'}),
            'Edad': forms.NumberInput(attrs={'class': 'inp1'}),
            'Civil': forms.Select(attrs={'class': 'inp2'}),
        }

class Form_educacion (forms.ModelForm):
    class Meta:
        model = Educacion
        fields = ['Archivo' , 'Nombre_Instituto' , 'Ano_graduacion' , 'Tiempo' , 'id']
        widgets = {
            'Archivo' : forms.FileInput (attrs={'class': 'inp3',
                                                'accept' : '.pdf',
                                                'id' : 'img',
                                                'required' : False
                                                }),
            'Nombre_Instituto' : forms.TextInput (attrs={'class' : 'inp'}),
            'Ano_graduacion' : Date (attrs={'class': 'inp2'}),
            'Tiempo' : forms.NumberInput (attrs= {'class' : 'inp1'}),
        }

class Form_Empresa (forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['Nombre_empresa' , 'Cargo' , 'Fecha_Inicio' , 'Fecha_Finalizacion' , 'Funciones']
        widgets = {
            'Nombre_empresa' : forms.TextInput (attrs={'class': 'inp',}),
            'Cargo' : forms.TextInput (attrs={'class' : 'inp'}),
            'Fecha_Inicio' : Date (attrs={'class': 'inp2'}),
            'Fecha_Finalizacion' : Date (attrs={'class': 'inp2'}),
            'Funciones' : forms.Textarea (attrs= {'id' : 'dsr'}),
        }

class Form_Refe_Person (forms.ModelForm):
    class Meta:
        model = Refe_personales
        fields = ['Nombre_person' , 'Apellido_person' , 'Direccion' , 'N_celular']
        widgets = {
            'Nombre_person' : forms.TextInput (attrs={'class': 'inp',}),
            'Apellido_person' : forms.TextInput (attrs={'class' : 'inp'}),
            'Direccion' : forms.TextInput (attrs={'class' : 'inp'}),
            'N_celular' : forms.NumberInput (attrs={'class': 'inp1'}),
        }

class Form_Refe_Empresarial (forms.ModelForm):
    class Meta:
        model = Refe_empresarial
        fields = '__all__'
        widgets = {
            'Nombre_Empresa' : forms.TextInput (attrs={'class': 'inp',}),
            'Nombre_Jefe' : forms.TextInput (attrs={'class' : 'inp'}),
            'Direccion' : forms.TextInput (attrs={'class' : 'inp'}),
            'N_celular' : forms.NumberInput (attrs={'class': 'inp1'}),
        }

class Form_Adicional (forms.ModelForm):
    class Meta:
        model= Informacion_Adicional
        fields = ['Inforamcion_adi']
        widgets = {
            'Inforamcion_adi' : forms.Textarea (attrs= {'id' : 'infoa'}),
        }
