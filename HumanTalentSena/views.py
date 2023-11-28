from django.shortcuts import render , redirect
from django.contrib import admin
from django.http import HttpResponse
def index (request):
    data = {
        'boton': botones(request),
        'barra' : barra (request),
    }
    return render(request , 'index.html' , data)

def registro (request):
    return render(request , 'registro.html')

def login(request):
    return render(request , 'login.html')

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
