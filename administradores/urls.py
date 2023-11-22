from django.urls import include, path 
from . import views

urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'),
    path('Editar_Usuarios/', views.usuariosedit, name='usuariosedit'),
    path('visualizar_users/', views.visualizar_tablas, name='visualizar'),
]