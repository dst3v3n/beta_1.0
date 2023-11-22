from django.shortcuts import render
from . models import Usuario , User
from . forms import Contact_Form
from HumanTalentSena.static.python.encriptar import encriptar
# Create your views here.

def visualizar (request):
    get_usuarios = Usuario.objects.all()
    data = {
        'get_usuarios': get_usuarios
    }

    return render(request , 'tabla_users.html' , data)

def metodo_post (request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        password = encriptar (password)
        Usuario(Nombre = nombre , Apellido = apellido , Email = email , Password = password).save ()
        return render(request , 'login.html')
    else:
        return (request , 'registro.html')  

def contac (request):
    contact_form = Contact_Form ()
    return render (request , 'crispy.html' , {'form' : contact_form})

def metodo_post_new (request):
    if request.method == "POST":
        nombre = request.POST['Nombre']
        apellido = request.POST['Apellido']
        fecha = request.POST['Fecha']
        documento = request.POST['Documento']
        User(Nombre = nombre , Apellido = apellido , Fecha = fecha , Documento = documento).save ()
        return render(request , 'index.html')
    else:
        return (request , 'crispy.html')  