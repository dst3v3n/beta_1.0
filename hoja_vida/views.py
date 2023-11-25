from django.shortcuts import render
from django.http import HttpResponse
from . models import Informacion_Person
from . forms import Form_Info_Person

# Create your views here.

def hoja_vida (request):
    form_info = Form_Info_Person ()
    return render (request , 'hoja_vida.html' , {'form' : form_info})

def post (request):
    if request.method == 'POST':
        nombre = request.POST ['nombre']
        apellido = request.POST ['apellido']
        direccion = request.POST ['direccion']
        cel = request.POST ['cel']
        email = request.POST ['email']
        fnacimiento = request.POST ['fnacimiento']
        tipod = request.POST ['tipod']
        ndoc = request.POST ['ndoc']
        genero = request.POST ['genero']
        edad = request.POST ['edad']
        civil = request.POST ['civil']
        usuario = Informacion_Person (nombre , apellido , direccion , cel , email , fnacimiento , tipod , ndoc , genero , edad , civil)
        usuario.save ()
    return render (request , 'hoja_vida.html' , {'usuario' : usuario})
    # return HttpResponse (f"{request.POST['civil']}")
