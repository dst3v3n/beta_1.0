from django.shortcuts import render , redirect
from . models import Usuario
from administradores.views import verificacion_admin
from HumanTalentSena.static.python.encriptar import encriptar
# Create your views here.

def visualizar (request):
    get_usuarios = Usuario.objects.all()
    data = {
        'get_usuarios': get_usuarios
    }

    return render(request , 'tabla_users.html' , data)

def verificacion (request):
    if  request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        verificacion = Usuario.objects.filter(Email = email).values  ()
        try:
            if len(verificacion) > 0:
                for user in verificacion:
                    user_id = user ['id']
                    email = user['Email']
                    passwd = user['Password']
                password = encriptar (password)
                if email == email and passwd == password:
                    context = {
                        'id' : user_id ,
                        'email' : email ,
                        'login_status' : True
                    }
                    response = redirect ('index')
                    response.set_cookie ('User_id' , user_id , secure=True , httponly=True , samesite='None')
                    response.set_cookie ('Email' , email , secure=True , httponly=True , samesite='None')
                    response.set_cookie ('Login_status' , True , secure=True , httponly=True , samesite='None')
                    return response
            else:
                return verificacion_admin (request , email , password)
        except:
            return redirect ('registro')

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

def perfil_user(request):
    return render(request , 'perfiluser.html')


def cerrar_sesion (request):
    response = redirect('index')
    response.delete_cookie('User_id')
    response.delete_cookie('Email')
    response.delete_cookie('Login_status')
    return response
