from django.urls import path
from . import views

urlpatterns = [
    path('filtrar' , views.filtrar_filtro , name='filtrar_filtro'),
    path('visualizar', views.visualizar_filtro , name='visualizar_filtro'),
]