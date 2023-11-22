from django.urls import path
from . import views

urlpatterns = [
    path('index/' , views.hoja_vida , name='hoja de vida'),
    # path('visualizar/' , views.visualizar , name='visualizar'),
]