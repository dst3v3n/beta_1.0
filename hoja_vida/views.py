from django.shortcuts import render , redirect
from . forms import Form_Info_Person , Form_educacion , Form_Empresa , Form_Refe_Person , Form_Refe_Empresarial , Form_Adicional
from . forms_disable import Form_Disable_Info_Person , Form_Disable_educacion , Form_Disable_Empresa , Form_Disable_Refe_Person , Form_Disable_Refe_Empresarial , Form_Disable_Form_Adicional
from . models import Informacion_Person , Educacion , Empresa , Refe_personales , Refe_empresarial , Informacion_Adicional

# Create your views here.

def hoja_vida (request):

    informacion = Informacion_Person.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    form_info_instance = Form_Info_Person (instance=informacion)

    adicional = Informacion_Adicional.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    form_adicio_instance = Form_Adicional (instance=adicional)

    list_educacion = []
    instancia = Educacion.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia) >= 1:
        for i in instancia:
            id_educacion = i['id']
            x =Educacion.objects.get(id = id_educacion)
            form_educacion_instance = Form_educacion (instance= x)
            list_educacion.append(form_educacion_instance)
    else:
        list_educacion.append (Form_educacion ())


    list_empresa = []
    instancia_1 = Empresa.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_1) >= 1:
        print (instancia_1)
        for i in instancia_1:
            id_empresa = i['id']
            x =Empresa.objects.get(id = id_empresa)
            form_empresa_instance = Form_Empresa (instance= x)
            list_empresa.append(form_empresa_instance)
    else:
        list_empresa.append (Form_Empresa ())

    list_personales = []
    instancia_2 = Refe_personales.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_2) >= 1:
        for i in instancia_2:
            id_person = i['id']
            x = Refe_personales.objects.get(id = id_person)
            form_personales_instance = Form_Refe_Person (instance= x)
            list_personales.append(form_personales_instance)
    else:
        for i in range(2):
            form_personales = Form_Refe_Person ()
            list_personales.append (form_personales)

    list_empresariales = []
    instancia_3 = Refe_empresarial.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_3) >= 1:
        for i in instancia_3:
            id_person = i['id']
            x = Refe_empresarial.objects.get(id = id_person)
            form_empresariales_instance = Form_Refe_Empresarial (instance= x)
            list_empresariales.append(form_empresariales_instance)
    else:
        for i in range(2):
            form_empresariales_instance = Form_Refe_Empresarial ()
            list_empresariales.append (form_empresariales_instance)

    form_empresa = Form_Empresa ()
    form_educacion = Form_educacion ()

    data =  {'form_info' : form_info_instance,
             'form_edu' : list_educacion,
             'form_empresa' : list_empresa,
             'form_person' : list_personales,
             'form_empresarial' : list_empresariales,
             'form_adicio' : form_adicio_instance,
             'form_edu_in' : form_educacion,
             'form_empresa_in' : form_empresa,
             }

    return render (request , 'hoja_vida.html' ,data)

def guardar_info (request):
    if request.method == 'POST':
        informacion = Informacion_Person.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
        form = Form_Info_Person(request.POST , instance=informacion)
        if form.is_valid():
            info = form.save(commit=False)
            info.Usuario_id = request.COOKIES.get('User_id')
            info.save()
            return redirect ('index_hoja')
        else:
            return redirect ('index_hoja')
    else:
        return redirect ('index_hoja')


def guardar_educacion (request):
    if request.method == 'POST':
        instancia = Educacion.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
        getlist = request.POST.getlist('Nombre_Instituto')
        if len(instancia) != len(getlist):
            form = Form_educacion(request.POST , request.FILES)
            if form.is_valid():
                info = form.save(commit=False)
                info.Usuario_id = request.COOKIES.get('User_id')
                info.save()
                return redirect ('index_hoja')

def guardar_empresa (request):
    if request.method == 'POST':
        instancia = Empresa.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
        getlist = request.POST.getlist('Nombre_empresa')
        if len(instancia) != len(getlist):
            for i in range(len(instancia) , len(getlist)):
                form = Form_Empresa(request.POST)
                if form.is_valid():
                    info = form.save(commit=False)
                    info.Usuario_id = request.COOKIES.get('User_id')
                    info.save()
                    return redirect ('index_hoja')
        else:
            form = Form_Empresa(request.POST)
            if form.is_valid():
                info = form.save(commit=False)
                info.Usuario_id = request.COOKIES.get('User_id')
                info.save()
                return redirect ('index_hoja')

def guardar_referencias_personales (request):
    if request.method == 'POST':
        getlist = request.POST.getlist('Nombre_person')
        getlist1 = request.POST.getlist('Nombre_Jefe')
        for i in range(len(getlist)):
            info = Refe_personales (Nombre_person = request.POST.getlist('Nombre_person')[i] , Apellido_person = request.POST.getlist('Apellido_person')[i] , Direccion = request.POST.getlist('Direccion')[i] , N_celular = request.POST.getlist ('N_celular')[i] , Usuario_id = request.COOKIES.get ('User_id'))
            info.save ()

        for h in range(len(getlist1)):
            info = Refe_empresarial (Nombre_Empresa = request.POST.getlist('Nombre_Empresa')[h] , Nombre_Jefe = request.POST.getlist('Nombre_Jefe')[h] , Direccion = request.POST.getlist('Direccion')[h] , N_celular = request.POST.getlist ('N_celular')[h] , Usuario_id = request.COOKIES.get ('User_id'))
            info.save ()
            return redirect ('index_hoja')

def guardar_info_adicional (request):
    print (request.method)
    if request.method == 'POST':
        print ('hola')
        form = Form_Adicional(request.POST)
        if form.is_valid():
            info = form.save(commit=False)
            info.Usuario_id = request.COOKIES.get('User_id')
            info.save()
            return redirect ('index_hoja')


def visualizar_hoja (request):

    informacion = Informacion_Person.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    form_info_instance = Form_Disable_Info_Person (instance=informacion)

    info = Informacion_Adicional.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    form_adicio_instance = Form_Disable_Form_Adicional (instance=info)

    list_educacion = []
    instancia = Educacion.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia) >= 1:
        for i in instancia:
            id_educacion = i['id']
            x =Educacion.objects.get(id = id_educacion)
            form_educacion_instance = Form_Disable_educacion (instance= x)
            list_educacion.append(form_educacion_instance)
    else:
        list_educacion = Form_Disable_educacion (instance=instancia)


    list_empresa = []
    instancia_1 = Empresa.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_1) >= 1:
        print (instancia_1)
        for i in instancia_1:
            id_empresa = i['id']
            x =Empresa.objects.get(id = id_empresa)
            form_empresa_instance = Form_Disable_Empresa (instance= x)
            list_empresa.append(form_empresa_instance)
    else:
        list_empresa.append (Form_Disable_Empresa ())

    list_personales = []
    instancia_2 = Refe_personales.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_2) >= 1:
        for i in instancia_2:
            id_person = i['id']
            x = Refe_personales.objects.get(id = id_person)
            form_personales_instance = Form_Disable_Refe_Person (instance= x)
            list_personales.append(form_personales_instance)
    else:
        for i in range(2):
            form_personales = Form_Disable_Refe_Person ()
            list_personales.append (form_personales)

    list_empresariales = []
    instancia_3 = Refe_empresarial.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_3) >= 1:
        for i in instancia_3:
            id_person = i['id']
            x = Refe_empresarial.objects.get(id = id_person)
            form_empresariales_instance = Form_Disable_Refe_Empresarial (instance= x)
            list_empresariales.append(form_empresariales_instance)
    else:
        for i in range(2):
            form_personales = Form_Disable_Refe_Empresarial ()
            list_empresariales.append (form_personales)

    data =  {'form_info' : form_info_instance,
             'form_edu' : list_educacion,
             'form_empresa' : list_empresa,
             'form_person' : list_personales,
             'form_empresarial' : list_empresariales,
             'form_adicio' : form_adicio_instance,
             }

    return render (request , 'hoja_vida_visualizar.html' , data)
