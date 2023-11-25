from django.urls import path
from . import views

urlpatterns = [
    path('index/' , views.hoja_vida , name='index_hoja'),
    path('hola' , views.post , name='hola')
]
