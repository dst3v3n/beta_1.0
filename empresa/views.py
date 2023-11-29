from django.shortcuts import render , redirect
from . models import Empresa
from .forms import FormularioEmpresa
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
