from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login_ajax',views.login_ajax,name='login_ajax'),
    path('', views.login, name='login'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_navbar', views.admin_navbar, name='admin_navbar'),
    path('admin_dashboard',views.admin_dashboard,name='admin_dashboard'),
    path('admin_staff', views.admin_staff, name='admin_staff'),
    path('admin_project', views.admin_project, name='admin_project'),
    path('admin_create_project', views.admin_create_project, name='admin_create_project'),
    path('admin_staff_email_registration', views.admin_staff_email_registration, name='admin_staff_email_registration'),
    path('admin_desig_save', views.admin_desig_save, name='admin_desig_save'),
    path('admin_staff_view_profile/<int:id>',views.admin_staff_view_profile,name='admin_staff_view_profile'),
    path('staff_activation/<int:id>',views.staff_activation,name="staff_activation"),
    path('staff_deactivation/<int:id>',views.staff_deactivation,name="staff_deactivation"),

    path('admin_staff_teams',views.admin_staff_teams,name='admin_staff_teams'),
    path('admin_staff_task',views.admin_staff_task,name='admin_staff_task'),

    path('admin_staff_attendance',views.admin_staff_attendance,name="admin_staff_attendance"),

    path('admin_staff_breaktimeview/<int:id>',views.admin_staff_breaktimeview,name="admin_staff_breaktimeview"),

    path('doings',views.admin_staff_whatdoing,name='admin_staff_whatdoing'),


]