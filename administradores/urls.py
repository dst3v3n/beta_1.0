from django.urls import path 
from . import views

urlpatterns = [
    path('', views.admin_index, name='admin_index'),
    path('visualizar_users/', views.visualizar_tablas, name='visualizar'),
    path('acceso/', views.verificacion , name="verificacion"),
    path('editarusuario/<int:id_usuario>',views.editarUsuario,name="editar_usuario"),
    path("actualizar_usuario/<int:id_usuario>",views.actualizarUsuario, name="actualizar_usuario"),
    path('registro/', views.admin_registra , name="registro_admin"),
]