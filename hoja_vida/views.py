from django.shortcuts import render , redirect
from . forms import Form_Info_Person , Form_educacion , Form_Empresa , Form_Refe_Person , Form_Refe_Empresarial , Form_Adicional
from . forms_disable import Form_Disable_Info_Person , Form_Disable_educacion , Form_Disable_Empresa , Form_Disable_Refe_Person , Form_Disable_Refe_Empresarial , Form_Disable_Adicional
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
    if len(instancia_3) == 2:
        for i in instancia_3:
            id_person = i['id']
            x = Refe_empresarial.objects.get(id = id_person)
            form_empresariales_instance = Form_Refe_Empresarial (instance= x)
            list_empresariales.append(form_empresariales_instance)
    elif len (instancia_3) == 1:
        adicional = Refe_empresarial.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
        list_empresariales.append (Form_Refe_Empresarial (instance=adicional))
        list_empresariales.append (Form_Refe_Empresarial ())
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
    if request.method == 'POST':
        informacion = Informacion_Adicional.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
        form = Form_Adicional(request.POST , instance=informacion)
        if form.is_valid():
            info = form.save(commit=False)
            info.Usuario_id = request.COOKIES.get('User_id')
            info.save()
            return redirect ('index_hoja')
        else:
            return redirect ('index_hoja')


def visualizar_hoja (request):

    informacion = Informacion_Person.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    form_info_instance = Form_Disable_Info_Person (instance=informacion)

    info = Informacion_Adicional.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
    form_adicio_instance = Form_Disable_Adicional (instance=info)

    list_educacion = []
    instancia = Educacion.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia) >= 1:
        for i in instancia:
            id_educacion = i['id']
            x =Educacion.objects.get(id = id_educacion)
            form_educacion_instance = Form_Disable_educacion (instance= x)
            list_educacion.append(form_educacion_instance)
    else:
        list_educacion.append (Form_Disable_educacion ())


    list_empresa = []
    instancia_1 = Empresa.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_1) >= 1:
        for i in instancia_1:
            id_empresa = i['id']
            x =Empresa.objects.get(id = id_empresa)
            form_active_empresa_instance = Form_Disable_Empresa (instance= x)
            list_empresa.append(form_active_empresa_instance)
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
            form_empresariales_instance = Form_Disable_Refe_Empresarial ()
            list_empresariales.append (form_empresariales_instance)

############################DIALOGO################################################

    form_active_info_instance = Form_Info_Person (instance=informacion)

    form_active_adicio_instance = Form_Adicional (instance=info)

    list_active_educacion = []
    instancia = Educacion.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia) >= 1:
        for i in instancia:
            id_educacion = i['id']
            x =Educacion.objects.get(id = id_educacion)
            form_active_educacion_instance = Form_educacion (instance= x)
            list_active_educacion.append(form_active_educacion_instance)
    else:
        list_active_educacion.append (Form_educacion ())


    list_active_empresa = []
    instancia_1 = Empresa.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_1) >= 1:
        for i in instancia_1:
            id_empresa = i['id']
            x =Empresa.objects.get(id = id_empresa)
            form_active_empresa_instance = Form_Empresa (instance= x)
            list_active_empresa.append(form_active_empresa_instance)
    else:
        list_active_empresa.append (Form_Empresa ())

    list_active_personales = []
    instancia_2 = Refe_personales.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_2) >= 1:
        for i in instancia_2:
            id_person = i['id']
            x = Refe_personales.objects.get(id = id_person)
            form_active_personales_instance = Form_Refe_Person (instance= x)
            list_active_personales.append(form_active_personales_instance)
    else:
        for i in range(2):
            form_personales = Form_Refe_Person ()
            list_active_personales.append (form_personales)

    list_active_empresariales = []
    instancia_3 = Refe_empresarial.objects.filter(Usuario_id = request.COOKIES.get('User_id')).values ()
    if len(instancia_3) >= 1:
        for i in instancia_3:
            id_person = i['id']
            x = Refe_empresarial.objects.get(id = id_person)
            form_active_empresariales_instance = Form_Refe_Empresarial (instance= x)
            list_active_empresariales.append(form_active_empresariales_instance)
    else:
        for i in range(2):
            form_active_empresariales_instance = Form_Refe_Empresarial ()
            list_active_empresariales.append (form_active_empresariales_instance)

######################VERIFICACION####################################

    if len(Informacion_Person.objects.filter(Usuario_id = request.COOKIES.get ('User_id'))) > 0:
        veri_info = True
    else:
        veri_info = False

    if len(Educacion.objects.filter(Usuario_id = request.COOKIES.get ('User_id'))) > 0:
        veri_edu = True
    else:
        veri_edu = False

    if len(Empresa.objects.filter(Usuario_id = request.COOKIES.get ('User_id'))) > 0:
        veri_empresa = True
    else:
        veri_empresa = False

    if len(Refe_personales.objects.filter(Usuario_id = request.COOKIES.get ('User_id'))) > 0:
        veri_personal = True
    else:
        veri_personal = False

    if len(Refe_empresarial.objects.filter(Usuario_id = request.COOKIES.get ('User_id'))) > 0:
        veri_empre = True
    else:
        veri_empre = False

    if len(Informacion_Adicional.objects.filter(Usuario_id = request.COOKIES.get ('User_id'))) > 0:
        veri_adicio = True
    else:
        veri_adicio = False

    data =  {'form_info' : form_info_instance,
             'form_edu' : list_educacion,
             'form_empresa' : list_empresa,
             'form_person' : list_personales,
             'form_empresarial' : list_empresariales,
             'form_adicio' : form_adicio_instance,
             ######
             'form_adicion_info' : form_active_info_instance,
             'form_adicion_edu' : list_active_educacion,
             'form_adicion_empresa' : list_active_empresa,
             'form_adicion_person' : list_active_personales,
             'form_adicion_empresarial' : list_active_empresariales,
             'form_adicion_adicio' : form_active_adicio_instance,
             #######
             'veri_info' : veri_info,
             'veri_edu' : veri_edu,
             'veri_empresa' : veri_empresa,
             'veri_person' : veri_personal,
             'veri_empre' : veri_empre,
             'veri_adicio' : veri_adicio,
             }

    return render (request , 'hoja_vida_visualizar.html' , data)


def editar_info (request):
    if request.method == 'POST':
        informacion = Informacion_Person.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
        form = Form_Info_Person(request.POST , instance=informacion)
        if form.is_valid():
            info = form.save(commit=False)
            info.Usuario_id = request.COOKIES.get('User_id')
            info.save()
            return redirect ('visualizar_hoja')

def editar_educacion (request , id_usuario):
    if request.method == 'POST':
        usuario = Educacion.objects.get (pk = id_usuario)
        form = Form_educacion (request.POST , instance= usuario)
        if form.is_valid ():
            info = form.save (commit = False)
            info.Usuario_id = request.COOKIES.get ('User_id')
            info.save ()
            return redirect ('visualizar_hoja')


def editar_empresa (request , id_usuario):
    if request.method == 'POST':
        usuario = Empresa.objects.get (pk = id_usuario)
        form = Form_Empresa (request.POST , instance= usuario)
        if form.is_valid ():
            info = form.save (commit = False)
            info.Usuario_id = request.COOKIES.get ('User_id')
            info.save ()
            return redirect ('visualizar_hoja')

def editar_referencias_personales (request , id_usuario):
    if request.method == 'POST':
        usuario = Refe_personales.objects.get (pk = id_usuario)
        form = Form_Refe_Person (request.POST , instance= usuario)
        if form.is_valid ():
            info = form.save (commit = False)
            info.Usuario_id = request.COOKIES.get ('User_id')
            info.save ()
            return redirect ('visualizar_hoja')

def editar_referencias_empresariales (request , id_usuario):
    usuario = Refe_empresarial.objects.get (pk = id_usuario)
    form = Form_Refe_Person (request.POST , instance= usuario)
    if form.is_valid ():
        info = form.save (commit = False)
        info.Usuario_id = request.COOKIES.get ('User_id')
        info.save ()
        return redirect ('visualizar_hoja')

def editar_info_adicional (request):
    if request.method == 'POST':
        informacion = Informacion_Adicional.objects.filter(Usuario_id=request.COOKIES.get ('User_id')).first()
        form = Form_Adicional(request.POST , instance=informacion)
        if form.is_valid():
            info = form.save(commit=False)
            info.Usuario_id = request.COOKIES.get('User_id')
            info.save()
            return redirect ('visualizar_hoja')

def eliminar_info (request):
    usuario = Informacion_Person.objects.get (Usuario_id = request.COOKIES.get('User_id'))
    usuario.delete ()
    return redirect ('visualizar_hoja')

def eliminar_educacion (request , id_usuario):
    usuario = Educacion.objects.get (pk = id_usuario)
    usuario.delete ()
    return redirect ('visualizar_hoja')

def eliminar_empresa (request , id_usuario):
    usuario = Empresa.objects.get (pk = id_usuario)
    usuario.delete ()
    return redirect ('visualizar_hoja')

def eliminar_referencais_personales (request , id_usuario):
    usuario = Refe_personales.objects.get (pk = id_usuario)
    usuario.delete ()
    return redirect ('visualizar_hoja')

def eliminar_referencias_empresariales (request , id_usuario):
    usuario = Refe_empresarial.objects.get (pk = id_usuario)
    usuario.delete ()
    return redirect ('visualizar_hoja')

def eliminar_adicional (request):
    usuario = Informacion_Adicional.objects.get (Usuario_id = request.COOKIES.get('User_id'))
    usuario.delete ()
    return redirect ('visualizar_hoja')
