from django.urls import path
from . import views

urlpatterns = [
    path('index/' , views.hoja_vida , name='index_hoja'),
    path('index/informacion', views.guardar_info , name='indexe'),
]
