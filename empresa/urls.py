from django.urls import path
from . import views


urlpatterns = [
    path('datos_empresa/' , views.metodo_post , name='datos_empresa'),
]
