"""
URL configuration for HumanTalentSena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', views.admministrar , name='admin_link'),
    path('', views.index , name="index"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login , name="login"),
    path('busqueda/', views.busqueda , name="busqueda"),
    path('usuarios/' , include('usuarios.urls')),
    path('admins/' , include('administradores.urls')),
    path('hoja_vida/' , include('hoja_vida.urls')),
]+static(settings.FOTOS_URL, document_root=settings.FOTOS_ROOT), +static(settings.FONDOS_URL, document_root=settings.FONDOS_ROOT)
