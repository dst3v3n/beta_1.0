from django.urls import path
from . import views


urlpatterns = [
    path('acceso_perfil/', views.iniciar_sesion , name="acceso_per"),
    path('perfil/' , views.mostrar_perfil , name='perfil_usuarios '),
]