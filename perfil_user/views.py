from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from usuarios.models import Usuario

def iniciar_sesion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        usuario = authenticate(email=email, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('perfil') 
        else:
            return render(request, 'login.html')

    return render(request, 'login.html')

@login_required
def mostrar_perfil(request):
    perfil_user = request.Usuario.Perfil  
    return render(request, 'perfiluser.html', {'perfil_user': perfil_user})

