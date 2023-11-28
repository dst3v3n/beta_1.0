from django.urls import path
from . import views


urlpatterns = [
    path('perfil/' , views.mostrar_perfil , name='perfil_usuarios '),
]