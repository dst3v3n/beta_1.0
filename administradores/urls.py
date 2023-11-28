from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_index, name='admin_index'),
    path('Editar_Usuarios/', views.usuariosedit, name='usuariosedit'),
    path('visualizar_users/', views.visualizar_tablas, name='visualizar'),
    path("eliminar_usuario/<int:id_usuario>",views.eliminarUsuario, name="eliminar_usuario"),
    path('editarusuario/<int:id_usuario>',views.editarUsuario,name="editar_usuario"),
    path("actualizar_usuario/<int:id_usuario>",views.actualizarUsuario, name="actualizar_usuario"),
    path('registro/', views.admin_registra , name="registro_admin"),
    path('dato_admins/', views.metodo_post , name="datos_admin"),
]
