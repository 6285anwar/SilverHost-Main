from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('logout',views.logout, name="logout"),
    path('staff_navbar',views.staff_navbar,name='staff_navbar'),
    path('staff_registrations/<int:des_id>/<str:text>/<str:code>',views.staff_registrations,name='staff_registrations'),
    path('save_staff_registration',views.save_staff_registration,name='save_staff_registration'),
    path('staff_dashboard',views.staff_dashboard,name='staff_dashboard'),
    path('staff_attendance',views.staff_attendance,name='staff_attendance'),
    path('staff_online/<int:id>',views.staff_online,name='staff_online'),
    path('staff_offline/<int:id>',views.staff_offline,name='staff_offline'),

    path('staff_first_half_attendance/<int:id>',views.staff_first_half_attendance,name='staff_first_half_attendance'),
    path('staff_fullday_attendance/<int:id>',views.staff_fullday_attendance,name='staff_fullday_attendance'),
    path('staff_fullday_attendance1/<int:id>',views.staff_fullday_attendance1,name='staff_fullday_attendance1'),

    path('staff_leave/<int:id>',views.staff_leave,name='staff_leave'),

    path('staff_work_report',views.staff_work_report,name='staff_work_report'),

    path('staff_task',views.staff_task,name='staff_task'),
    path('staff_work_accept/<int:id>',views.staff_work_accept,name="staff_work_accept"),
    path('staff_task_report/<int:id>',views.staff_task_report,name='staff_task_report'),
    path('staff_profile',views.staff_profile,name='staff_profile'),
    path('staff_settings',views.staff_settings,name='staff_settings'),

    path('staffadd_staff_task/<int:id>',views.staffadd_staff_task, name="staffadd_staff_task"),


    path('staff_checkin/<int:id>',views.staff_checkin,name='staff_checkin'),
    path('staff_checkout/<int:id>',views.staff_checkout,name='staff_checkout'),
    path('staff_teatime/<int:id>',views.staff_teatime,name='staff_teatime'),
    path('staff_lunchtime/<int:id>',views.staff_lunchtime,name='staff_lunchtime'),
    path('staff_overtime/<int:id>',views.staff_overtime,name='staff_overtime'),


    path('staff_project_doing/<int:id>',views.staff_project_doing,name="staff_project_doing"),
    path('staff_task_doing/<int:id>',views.staff_task_doing,name="staff_task_doing"),
    path('staff_clear_doing/<int:id>',views.staff_clear_doing,name="staff_clear_doing"),


    path('staff_task_view/<int:id>',views.staff_task_view,name="staff_task_view"),
    path('staff_task_cancelled/<int:id>',views.staff_task_cancelled,name="staff_task_cancelled"),

    path('satff_task_edit/<int:id>',views.satff_task_edit,name="satff_task_edit"),
    path('staff_task_edit_save/<int:id>',views.staff_task_edit_save,name="staff_task_edit_save"),







    path('staff_attend_breaktimestart',views.staff_attend_breaktimestart,name="staff_attend_breaktimestart"),
    path('staff_attend_breaktimeend',views.staff_attend_breaktimeend,name="staff_attend_breaktimeend"),





]