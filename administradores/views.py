from django.shortcuts import render
from . models import Usuario

# Create your views here.
def admin_index(request):
    return render(request , 'admin_index.html')

def visualizar (request):
    get_usuarios = Usuario.objects.all()
    data = {
        'get_usuarios': get_usuarios
    }

    return render(request , 'tabla_users.html' , data)
