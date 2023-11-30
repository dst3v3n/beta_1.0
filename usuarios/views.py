from django.shortcuts import render , redirect
from . models import Usuario
from .forms import FormularioUsario
from empresa.views import verificacion_empresa
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
        if len(verificacion) > 0:
            for user in verificacion:
                user_id = user ['id']
                email = user['Email']
                passwd = user['Password']
            password = encriptar (password)
            if email == email and passwd == password:
                response = redirect ('index')
                response.set_cookie ('User_id' , user_id , secure=True , httponly=True , samesite='None')
                response.set_cookie ('Email' , email , secure=True , httponly=True , samesite='None')
                response.set_cookie ('tipo_usuario' , 'Usuario' , secure=True , httponly=True , samesite='None')
                response.set_cookie ('Login_status' , True , secure=True , httponly=True , samesite='None')
                return response
        else:
            return verificacion_empresa (request , email , password)
def metodo_post (request):
    if request.method == "POST":
        password = request.POST['Password']
        re_password = request.POST['re_password']
        if password == re_password:
            password = encriptar (password)
            new_usuario = FormularioUsario (request.POST)
            if new_usuario.is_valid ():
                info = new_usuario.save (commit=False)
                info.Password = password
                info.save ()
                return redirect ('login')
    else:
        return (request , 'registro.html')

def perfil_user(request):
    return render(request , 'perfiluser.html')
