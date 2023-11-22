from django.urls import include, path 
from . import views

urlpatterns = [
    path('admin_index/', views.admin_index, name='admin_index'),
    path('visualizar_users/', views.visualizar_tablas, name='visualizar'),
    path('acceso/', views.verificacion , name="verificacion"),
    path('editarusuario/<int:id_usuario>',views.editarUsuario,name="editar_usuario"),
    path("actualizar_usuario/<int:id_usuario>",views.actualizarUsuario, name="actualizar_usuario"),
]