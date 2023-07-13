from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [


    path('navbar',views.crm_navbar, name="navbar"),
    path('dashboard',views.crm_dashboard, name="dashboard"),
    path('clients',views.crm_clients,name="clients"),
    path('add_client',views.crm_add_client,name="add_client"),


]