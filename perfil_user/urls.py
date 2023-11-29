from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('perfil/' , views.mostrar_perfil , name='perfil_usuarios '),
]
if settings.DEBUG:
        urlpatterns += static(settings.FOTOS_URL,
                            document_root=settings.FOTOS_ROOT)
if settings.DEBUG:
        urlpatterns += static(settings.FONDOS_URL,
                            document_root=settings.FONDOS_ROOT)