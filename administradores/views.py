from django.shortcuts import render
from usuarios.models import Usuario
from .models import Admin
from HumanTalentSena.static.python.encriptar import encriptar

# Create your views here.
def admin_index(request):
    return render(request , 'admin_index.html')

def visualizar_tablas (request):
    get_usuarios = Usuario.objects.all()
    data = {
        'get_usuarios' : get_usuarios
    }
    return render (request , 'tabla_users.html' , data)

def verificacion (request):
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        verificacion = Admin.objects.filter(Email = email).values ()
        if len(verificacion) > 0: 
            for user in verificacion:
                Email = user['Email']
                passwd = user['Password']
            # password = encriptar (password)
            if Email == email and passwd == password:
                return render (request , 'admin_index.html')
        else:
            verificacion = Usuario.objects.filter(Email = email).values  ()
            for user in verificacion:
                Email = user['Email']
                passwd = user['Password']
            password = encriptar (password)
            if Email == email and passwd == password:
                return render (request , 'index.html')

def eliminarUsuario(request, id_usuario):
    user=Usuario.objects.get(pk=id_usuario)
    user.delete()
    usuarios=Usuario.objects.all()
    return render(request, "tabla_users.html",{"get_usuarios":usuarios})
