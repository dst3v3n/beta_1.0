from django.urls import include, path 
from . import views

urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'),
    path('visualizar_users/', views.visualizar_tablas, name='visualizar'),
    path('acceso/', views.verificacion , name="verificacion"),
    path("eliminar_usuario/<int:id_usuario>",views.eliminarUsuario, name="eliminar_usuario"),
]