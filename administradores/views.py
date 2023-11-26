from django.shortcuts import render
from django.http import HttpResponse
from usuarios.models import Usuario
from .models import Admin
from HumanTalentSena.static.python.encriptar import encriptar
from .forms import FormularioAdmin

# Create your views here.
def admin_index(request):
    return render(request , 'admin_index.html')

def visualizar_tablas (request):
    get_usuarios = Usuario.objects.all()
    data = {
        'get_usuarios' : get_usuarios
    }
    return render (request , 'tabla_users.html' , data)

def eliminarUsuario(request, id_usuario):
    user=Usuario.objects.get(pk=id_usuario)
    user.delete()
    usuarios=Usuario.objects.all()
    return render(request, "tabla_users.html",{"get_usuarios":usuarios})


def editarUsuario(request,id_usuario):
    usuario=Usuario.objects.filter(id=id_usuario).first()
    form=FormularioAdmin(instance=usuario)
    return render(request, "usuarioEdit.html",{"form":form,"usuario":usuario})

def actualizarUsuario(request,id_usuario):
    password = encriptar(request.POST["Password"])
    repassword = encriptar (request.POST["re_password"])
    usuario=Usuario.objects.get(pk=id_usuario)
    form=FormularioAdmin(request.POST,instance=usuario)
    if form.is_valid():
        usuario.encriptacion (password)
        if password == repassword:
            form.save()
            get_usuarios=Usuario.objects.all()
            return render(request,"tabla_users.html",{"get_usuarios":get_usuarios})

def admin_registra(request):
    return render(request , 'registro_admin.html')

def metodo_post (request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        password = request.POST['password']
        password = encriptar (password)
        Admin(Nombre = nombre , Apellido = apellido , Email = email , Password = password).save ()
        return render(request , 'admin_index.html')
    else:
        return (request , 'registro_admin.html')


def  usuariosedit(request):
    return render(request , 'usuarioEdit.html')

def verificacion_admin (request , email , password):
    verificacion = Admin.objects.filter(Email = email).values ()
    for user in verificacion:
        Email = user['Email']
        passwd = user['Password']
    password = encriptar (password)
    if Email == email and passwd == password:
        context = {
                    'email' : Email ,
                    'login_status' : True
                }
        response = render (request , 'admin_index.html' , context)
        response.set_cookie ('Email' , email)
        response.set_cookie ('login_status' , True)
        return response
    else:
        return render(request , 'login.html')
