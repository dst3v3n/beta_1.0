from django.shortcuts import render , redirect
from django.contrib import admin
from usuarios.forms import FormularioUsario
from empresa.forms import FormularioEmpresa

def index (request):
    data = {
        'boton': botones(request),
        'barra' : barra (request),
    }
    return render(request , 'index.html' , data)

def registro (request):
    data = {
        'Form_Usuario' : FormularioUsario ,
        'Form_Empresa' : FormularioEmpresa ,
    }
    return render(request , 'registro.html' , data)

def login(request):
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
