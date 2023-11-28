from django.urls import path
from . import views


urlpatterns = [
    path('login_perfil/', views.iniciar_sesion , name="login_per"),
    path('perfil/' , views.mostrar_perfil , name='perfil_usuarios '),
]