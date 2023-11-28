from django.shortcuts import render

# Create your views here.


from django.contrib.auth.decorators import login
from django.contrib.auth import authenticate, login

from buscador.models import Filtro



def filtrar_filtro(request):
    if request.method == 'POST':
            Rango_salario = request.POST['Rango_salario']
            Tipo_ocupacion = request.POST['Tipo_ocupacion']
            Ubicacion = request.POST['Ubicacion']
            Rango_exp= request.POST['Rango_exp']
            
    return render(request, 'buscador.html')

def visualizar_filtro (request):
    get_filtro = Filtro.objects.all()
    data = {
        'get_filtro': get_filtro
    }

    return render(request , 'buscador.html' , data)


   