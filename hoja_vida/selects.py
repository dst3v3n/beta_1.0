class Informacion_Per ():
    def documento ():

        select_documento = [('C.C' , 'C.C'),
                            ('C.E' , 'C.E'),
                            ('PAS' , 'PAS'),
                            ('TI' , 'TI')
                            ]

        return select_documento

    def genero ():

        select_genero = [('Masculino' , 'Masculino'),
                        ('Femenino' ,'Femenino')
                        ]

        return select_genero

    def estado_civil ():

        select_civil = [('Casado' , 'Casado'),
                        ('Union libre' , 'Union libre'),
                        ('Soltero' , 'Soltero')
                        ]

        return select_civil
