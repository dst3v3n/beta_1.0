from django.shortcuts import render , redirect
from . models import Empresa
from .forms import FormularioEmpresa
from administradores.views import verificacion_admin
from HumanTalentSena.static.python.encriptar import encriptar

# Create your views here.

def metodo_post (request):
    if request.method == "POST":
        password = request.POST['Password']
        re_password = request.POST['re_password']
        if password == re_password:
            password = encriptar (password)
            new_empresa = FormularioEmpresa (request.POST)
            if new_empresa.is_valid ():
                info = new_empresa.save (commit=False)
                info.Password = password
                info.save ()
            return redirect('login')
    else:
        return (request , 'registro.html')

def verificacion_empresa (request , email , password):
    verificacion = Empresa.objects.filter(Email = email).values ()
    if len(verificacion)> 0 :
        for user in verificacion:
            Email = user['Email']
            passwd = user['Password']
            user_id = user ['id']
        password = encriptar (password)
        if Email == email and passwd == password:
            response = redirect ('index')
            response.set_cookie ('User_id' , user_id , secure=True , httponly=True , samesite='None')
            response.set_cookie ('Email' , email , secure=True , httponly=True , samesite='None')
            response.set_cookie ('type_user' , 'Empresa' , secure=True , httponly=True , samesite='None')
            response.set_cookie ('Login_status' , True , secure=True , httponly=True , samesite='None')
            return response
    else:
        return verificacion_admin (request , email , password)
