from django import forms
from . models import Informacion_Person , Educacion , Empresa , Refe_personales , Refe_empresarial

class Date (forms.DateInput):
    input_type = 'date'

class Form_Disable_Info_Person (forms.ModelForm):
    class Meta:
        model = Informacion_Person
        fields = '__all__'
        widgets = {
            'Nombre': forms.TextInput(attrs={'class': 'inp',
                                             'readonly' :True
                                             }),
            'Apellido': forms.TextInput(attrs={'class': 'inp',
                                                'readonly' :True
                                                }),
            'Direccion': forms.TextInput(attrs={'class': 'inp',
                                                'readonly' :True
                                                }),
            'Celular' : forms.NumberInput (attrs={'class': 'inp1',
                                                'readonly' :True
                                                }),
            'Email' : forms.EmailInput (attrs={'class': 'inp',
                                                'readonly' :True
                                                }),
            'Fecha' : Date (attrs={'class': 'inp2',
                                   'readonly' :True
                                   }),
            'Tipod': forms.Select(attrs={'class': 'inp2',
                                                'readonly' :True
                                                }),
            'N_documento' : forms.NumberInput (attrs={'class': 'inp1',
                                                'readonly' :True
                                                }),
            'Genero': forms.Select(attrs={'class': 'inp2',
                                                'readonly' :True
                                                }),
            'Edad': forms.NumberInput(attrs={'class': 'inp1',
                                                'readonly' :True
                                                }),
            'Civil': forms.Select(attrs={'class': 'inp2',
                                                'readonly' :True
                                                }),
        }

class Form_Disable_educacion (forms.ModelForm):
    class Meta:
        model = Educacion
        fields = '__all__'
        widgets = {
            'Archivo' : forms.FileInput (attrs={'class': 'inp3',
                                                'accept' : '.pdf',
                                                'id' : 'img',
                                                'readonly' :True

                                                }),
            'Nombre_Instituto' : forms.TextInput (attrs={'class' : 'inp',
                                                         'readonly' :True
                                                         }),
            'Ano_graduacion' : Date (attrs={'class': 'inp2',
                                            'readonly' :True
                                            }),
            'Tiempo' : forms.NumberInput (attrs= {'class' : 'inp1',
                                                  'readonly' :True
                                                  }),
        }

class Form_Disable_Empresa (forms.ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'
        widgets = {
            'Nombre_empresa' : forms.TextInput (attrs={'class': 'inp',
                                                        'readonly' :True
                                                        }),
            'Cargo' : forms.TextInput (attrs={'class' : 'inp',
                                                'readonly' :True
                                                }),
            'Fecha_Inicio' : Date (attrs={'class': 'inp2',
                                          'readonly' :True
                                          }),
            'Fecha_Finalizacion' : Date (attrs={'class': 'inp2',
                                                'readonly' :True
                                                }),
            'Funciones' : forms.Textarea (attrs= {'id' : 'dsr',
                                                  'readonly' :True
                                                  }),
        }

class Form_Disable_Refe_Person (forms.ModelForm):
    class Meta:
        model = Refe_personales
        fields = '__all__'
        widgets = {
            'Nombre_person' : forms.TextInput (attrs={'class': 'inp',
                                                      'readonly' :True
                                                      }),
            'Apellido_person' : forms.TextInput (attrs={'class' : 'inp',
                                                        'readonly' :True
                                                        }),
            'Direccion' : forms.TextInput (attrs={'class' : 'inp',
                                                  'readonly' :True
                                                  }),
            'N_celular' : forms.NumberInput (attrs={'class': 'inp1',
                                                    'readonly' :True
                                                    }),
            'Inforamcion_adi' : forms.Textarea (attrs= {'id' : 'infoa',
                                                        'readonly' :True
                                                        }),
        }

class Form_Disable_Refe_Empresarial (forms.ModelForm):
    class Meta:
        model = Refe_empresarial
        fields = '__all__'
        widgets = {
            'Nombre_Empresa' : forms.TextInput (attrs={'class': 'inp',
                                                       'readonly' :True
                                                       }),
            'Nombre_Jefe' : forms.TextInput (attrs={'class' : 'inp',
                                                    'readonly' :True
                                                    }),
            'Direccion' : forms.TextInput (attrs={'class' : 'inp',
                                                  'readonly' :True
                                                  }),
            'N_celular' : forms.NumberInput (attrs={'class': 'inp1',
                                                    'readonly' :True
                                                    }),
        }
