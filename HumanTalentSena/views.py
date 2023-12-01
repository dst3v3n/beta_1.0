from django.shortcuts import render , redirect
from django.contrib import admin
from usuarios.forms import FormularioUsario
from empresa.forms import FormularioEmpresa

def index (request):
    if request.COOKIES.get ('type_user') == 'Admin':
        return redirect ('admin_index')
    else:
        data = {
            'boton': botones(request),
            'barra' : barra (request),
            'empresa' : acceso_empresa(request),
        }
        return render(request , 'index.html' , data)

def registro (request):
    if request.COOKIES.get ('Login_status') == 'True':
        return redirect ('index')
    else:
        data = {
            'Form_Usuario' : FormularioUsario ,
            'Form_Empresa' : FormularioEmpresa ,
        }
        return render(request , 'registro.html' , data)

def login(request):
    if request.COOKIES.get ('Login_status') == 'True':
        return redirect ('index')
    else:
        return render(request , 'login.html')

def busqueda(request):
    return render(request , 'busqueda.html')

def admministrar(request):
    return (request , admin.site.urls)

def botones (request):
    try:
        if request.COOKIES['Login_status']:
            return False
    except:
        return True

def barra (request):
    try:
        if request.COOKIES['Login_status']:
            return True
    except:
        return False

def cerrar_sesion (request):
    response = redirect('index')
    response.delete_cookie('User_id')
    response.delete_cookie('type_user')
    response.delete_cookie('Email')
    response.delete_cookie('Login_status')
    return response

def acceso_empresa (request):
    try:
        if request.COOKIES ['type_user'] == 'Empresa':
            return True
    except:
        return False
