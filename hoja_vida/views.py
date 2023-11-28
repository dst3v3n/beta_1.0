from django.shortcuts import render
from django.http import HttpResponse
from . forms import Form_Info_Person , Form_educacion , Form_Empresa , Form_Refe_Person , Form_Refe_Empresarial

# Create your views here.

def hoja_vida (request):
    form_info = Form_Info_Person ()
    form_educacion = Form_educacion ()
    form_empresa = Form_Empresa ()
    form_refe_person = Form_Refe_Person ()
    form_refe_empre = Form_Refe_Empresarial ()
    return render (request , 'hoja_vida.html' , {'form_info' : form_info ,
                                                 'form_edu' : form_educacion,
                                                 'form_empresa' : form_empresa,
                                                 'form_person' : form_refe_person,
                                                 'form_empresarial' : form_refe_empre})

def guardar_info (request):
    if request.method == 'POST':
        usuario = Form_Info_Person(request.POST)
        if usuario.is_valid():
            usuario.save()
            usuario=Form_Info_Person()
            form_info = Form_Info_Person ()
            form_educacion = Form_educacion ()
            form_empresa = Form_Empresa ()
            form_refe_person = Form_Refe_Person ()
            form_refe_empre = Form_Refe_Empresarial ()
    return render (request , 'hoja_vida.html' , {'form_info' : form_info ,
                                                 'form_edu' : form_educacion,
                                                 'form_empresa' : form_empresa,
                                                 'form_person' : form_refe_person,
                                                 'form_empresarial' : form_refe_empre})
