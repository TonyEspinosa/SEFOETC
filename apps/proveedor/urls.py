from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.v_prov, name="u_prov_list"),
    path('new', views.v_prov_new, name="u_prov_new"),
    path('upd/<str:pk_prov>/', views.v_prov_upd, name="u_prov_upd"),
    path('del/<str:pk_prov>/', views.v_prov_del, name="u_prov_del"),

    path('export_excel', views.v_export_excel, name="u_export_excel_prov"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)