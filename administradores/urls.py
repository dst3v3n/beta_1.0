from django.urls import include, path 
from . import views

urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'),
    path('visualizar/' , views.visualizar , name='visualizar_usuarios '),
    path('usuarios/' , include('usuarios.urls')),
    
    
]