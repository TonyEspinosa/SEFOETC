"""SEFOET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.urls import include

from django.conf.urls.static import static
from django.conf import settings

#Importar las vistas del proyecto
from . import views
from apps.usuario.views import v_usr_login, v_usr_logout

urlpatterns = [
    path('admin/', admin.site.urls),

    ## Páginas publicas
    path('', views.v_home, name = "u_home"),
    path('lista/<str:pk_cat>/', views.v_list, name = "u_list"),
    path('pdf_view/<str:pk_prov>/', views.v_ViewPDF, name="u_pdf_view"),

    path('export_excel/<str:pk_cat>/', views.v_export_excel, name="u_export_excel"),

    
    ## Paginas Privadas

    #inicio
    path('inicio/', views.v_inicio, name="u_home_priv"),
    path('login/', v_usr_login, name="u_usr_login"),
    path('logout/', v_usr_logout, name="u_usr_logout"),

    #App categoria
    path('cat/', include('apps.categoria.urls')),

    #App proveedor
    path('prov/', include('apps.proveedor.urls')),

    #App usuario
    path('usr/', include('apps.usuario.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)