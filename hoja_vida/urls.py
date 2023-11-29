from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('index/' , views.hoja_vida , name='index_hoja'),
    path('index/informacion', views.guardar_info , name='save_info'),
    path('index/educacion', views.guardar_educacion , name='save_educacion'),
    path('visualizar', views.visualizar_hoja , name='visualizar_hoja'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
