from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.v_cat, name="u_cat_list"),
    path('new', views.v_cat_new, name="u_cat_new"),
    path('upd/<str:pk_cat>/', views.v_cat_upd, name="u_cat_upd"),
    path('del/<str:pk_cat>/', views.v_cat_del, name="u_cat_del"),

    path('export_excel', views.v_export_excel, name="u_export_excel_cat"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)