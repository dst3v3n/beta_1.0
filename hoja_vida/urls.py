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
] +static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
