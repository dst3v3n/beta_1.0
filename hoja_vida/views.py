from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def hoja_vida (request):
    return render (request , 'hoja_vida.html')

def visualizar (request):
    hola = request.POST['hola']
    return HttpResponse (request.POST)
    