from django.shortcuts import render
from usuarios.models import Usuario

# Create your views here.
def admin_index(request):
    return render(request , 'admin_index.html')

def visualizar_tablas (request):
    get_usuarios = Usuario.objects.all()
    data = {
        'get_usuarios' : get_usuarios
    }
    return render (request , 'tabla_users.html' , data)

def registro (request):
    return render(request , 'registro.html')