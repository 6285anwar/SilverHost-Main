from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(staff_registration)
admin.site.register(staff_login_otp)
admin.site.register(attendance)
admin.site.register(staff_tasks)
admin.site.register(Staff_Project_Task_Reports)
admin.site.register(Attendance_Day_Break)


