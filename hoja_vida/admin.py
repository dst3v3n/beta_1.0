from django.contrib import admin
from . models import Informacion_Person , Educacion , Empresa , Refe_personales , Refe_empresarial
# Register your models here.

admin.site.register (Informacion_Person)
admin.site.register (Educacion)
admin.site.register (Empresa)
admin.site.register (Refe_personales)
admin.site.register (Refe_empresarial)
