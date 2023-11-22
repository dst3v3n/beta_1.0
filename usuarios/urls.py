from django.urls import path
from . import views


urlpatterns = [
    path('visualizar/' , views.visualizar , name='visualizar_usuarios '),
    path('datos/' , views.metodo_post , name='datos'),
]