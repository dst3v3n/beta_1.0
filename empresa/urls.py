from django.urls import path
from . import views

urlpatterns = [
    path('inf_empresa/' , views.empresa , name='index_empresa'),
]