from django.urls import path
from . import views

urlpatterns = [
    path('', views.v_usr, name="u_usr_list"),
    path('new', views.v_usr_new, name="u_usr_new"),
    path('upd/<str:pk_usr>/', views.v_usr_upd, name="u_usr_upd"),
    path('del/<str:pk_usr>/', views.v_usr_del, name="u_usr_del"),
    path('chng/<str:pk_usr>/', views.v_usr_chng, name="u_usr_chng"),

    path('export_excel', views.v_export_excel, name="u_export_excel_usr"),
]