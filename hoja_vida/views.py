from django.shortcuts import render , redirect
from . forms import Form_Info_Person , Form_educacion , Form_Empresa , Form_Refe_Person , Form_Refe_Empresarial
from . forms_disable import Form_Disable_Info_Person , Form_Disable_educacion , Form_Disable_Empresa , Form_Disable_Refe_Person , Form_Disable_Refe_Empresarial
from . models import Informacion_Person , Educacion , Empresa , Refe_personales , Refe_empresarial

# Create your views here.

def hoja_vida (request):
    informacion = Informacion_Person.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    educacion = Educacion.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    empresa = Empresa.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    personales = Refe_personales.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    empresariales = Refe_empresarial.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()

    form_info = Form_Info_Person (instance=informacion)
    form_educacion = Form_educacion (instance=educacion)
    form_empresa = Form_Empresa (instance=empresa)
    form_refe_person = Form_Refe_Person (instance=personales)
    form_refe_empre = Form_Refe_Empresarial (instance=empresariales)
    return render (request , 'hoja_vida.html' , {'form_info' : form_info ,
                                                 'form_edu' : form_educacion,
                                                 'form_empresa' : form_empresa,
                                                 'form_person' : form_refe_person,
                                                 'form_empresarial' : form_refe_empre})

def guardar_info (request):
    if request.method == 'POST':
        form = Form_Info_Person(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.Usuario_id = request.COOKIES.get('User_id')
            info.save()
            return redirect ('index_hoja')
        else:
            return redirect ('index_hoja')

def guardar_educacion (request):
    if request.method == 'POST':
        form = Form_educacion(request.POST , request.FILES)
        if form.is_valid():
            info = form.save(commit=False)
            info.Usuario_id = request.COOKIES.get('User_id')
            info.save()
            return redirect ('index_hoja')
        else:
            return redirect ('index_hoja')

def visualizar_hoja (request):
    informacion = Informacion_Person.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    educacion = Educacion.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    empresa = Empresa.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    personales = Refe_personales.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    empresariales = Refe_empresarial.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()

    form_info = Form_Disable_Info_Person (instance=informacion)
    form_educacion = Form_Disable_educacion (instance=educacion)
    form_empresa = Form_Disable_Empresa (instance=empresa)
    form_refe_person = Form_Disable_Refe_Person (instance=personales)
    form_refe_empre = Form_Disable_Refe_Empresarial (instance=empresariales)
    return render (request , 'hoja_vida_visualizar.html' , {'form_info' : form_info ,
                                                 'form_edu' : form_educacion,
                                                 'form_empresa' : form_empresa,
                                                 'form_person' : form_refe_person,
                                                 'form_empresarial' : form_refe_empre})
