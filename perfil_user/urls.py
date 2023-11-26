from django.urls import path
from . import views


urlpatterns = [
    path('perfil/' , views.visualizar , name='perfil_usuarios '),
]