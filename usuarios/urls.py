from django.urls import path
from . import views


urlpatterns = [
    path('visualizar/' , views.visualizar , name='visualizar_usuarios '),
    path('datos/' , views.metodo_post , name='datos'),
    path('perfil/' , views.perfil_user , name="perfil_user"),
    path('acceso/', views.verificacion , name="verificacion"),
]
