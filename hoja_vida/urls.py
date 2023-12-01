from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index/' , views.hoja_vida , name='index_hoja'),
    path('index/informacion', views.guardar_info , name='save_info'),
    path('index/educacion', views.guardar_educacion , name='save_educacion'),
    path('index/empresa', views.guardar_empresa , name='save_empresa'),
    path('index/referencias', views.guardar_referencias_personales , name='save_referencias'),
    path('index/adicional', views.guardar_info_adicional , name='save_adicional'),
    path('visualizar', views.visualizar_hoja , name='visualizar_hoja'),

    path('actualizar/informacion' , views.editar_info , name='editar_info'),
    path('actualizar/educacion/<int:id_usuario>/' , views.editar_educacion , name='ediar_educacion'),
    path('actualizar/empresa/<int:id_usuario>/' , views.editar_empresa , name='ediar_empresa'),
    path('actualizar/referencias/<int:id_usuario>/' , views.editar_referencias_personales , name='ediar_referencias_personales'),
    path('actualizar/referencias/<int:id_usuario>/' , views.editar_referencias_empresariales , name='ediar_referencias_empresariales'),
    path('actualizar/adicional' , views.editar_info_adicional , name='ediar_adicional'),

    path('eliminar/informacion' , views.eliminar_info , name='eliminar_info'),
    path('eliminar/educacion/<int:id_usuario>/' , views.eliminar_educacion , name='eliminar_educacion'),
    path('eliminar/empresa/<int:id_usuario>/' , views.eliminar_empresa , name='eliminar_empresa'),
    path('eliminar/referencias_personales/<int:id_usuario>/' , views.eliminar_referencais_personales , name='eliminar_referencias_personales'),
    path('eliminar/referencias_empresariales/<int:id_usuario>/' , views.eliminar_referencias_empresariales , name='eliminar_referencias_empresariales'),
    path('eliminar/adicional' , views.eliminar_adicional , name='eliminar_adicional'),
] +static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
