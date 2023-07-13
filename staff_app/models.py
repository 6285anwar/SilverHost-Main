from django.db import models
from admin_app.models import designation
# Create your models here.



class staff_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.CASCADE,null=True, blank=True)
    employee_id = models.CharField(max_length=240,null=True,default='')
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)

    address = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    
    email = models.EmailField(max_length=240, null=True)
    username = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    attitude = models.IntegerField(default='0')
    creativity = models.IntegerField(default='0')
    workperformance = models.IntegerField(default='0')
    joiningdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=True, auto_now=False,  null=True, blank=True)

    status = models.CharField(max_length=240, null=True)


    total_pay=models.IntegerField(default='0')
    payment_balance = models.IntegerField( default='0')
    account_no = models.CharField(max_length=200, null=True,blank=True, default='')
    account_name = models.CharField(max_length=200, null=True,blank=True, default='')
    ifsc =  models.CharField(max_length=200, null=True, default='')
    bank_name = models.CharField(max_length=240, null=True,blank=True, default='')
    bank_branch = models.CharField(max_length=240, null=True, default='') 
    payment_status = models.CharField(max_length=200, null=True, default='')
    google_pay = models.CharField(max_length=500, default='',null=True,blank=True)
    paypal = models.CharField(max_length=500, default='',null=True,blank=True)
    applepay = models.CharField(max_length=500, default='',null=True,blank=True)


    confirm_salary = models.IntegerField(default='0')
    confirm_salary_status = models.CharField(max_length=255, default='0')

    payment_file_downlod = models.FileField(upload_to = 'images/', null=True, blank=True)
    total_amount=models.IntegerField(default='0')
    payment_amount_date =models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    salary_pending = models.CharField(max_length=100, default='')
    salary_status =  models.CharField(max_length=10, default='')

    reg_status =  models.CharField(max_length=10, default='0')
    aadhar_no =  models.CharField(max_length=20, default='0')

    attendance_status =  models.CharField(max_length=10, default='0')
    checkin_status = models.CharField(max_length=10, default='0')
    

    he_is_a = models.CharField(max_length=10, default='DEVELOPER')

    iam_doing = models.CharField(max_length=200, default='')

 
    def __str__(self):
        return self.fullname

class staff_login_otp(models.Model):
    email = models.CharField(max_length=200,null=True)
    otp = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.email 


class attendance(models.Model):
    staff = models.ForeignKey(staff_registration, on_delete=models.CASCADE,null=True, blank=True)
    checkin_time = models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    checkout_time = models.TimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=200,null=True)
    attendance_status = models.CharField(max_length=200,null=True)

    start_time = models.DateTimeField(null=True, blank=True,)
    end_time = models.DateTimeField(null=True, blank=True)

    today_work = models.CharField(max_length=200,null=True,default='0')
    work_report = models.CharField(max_length=200,null=True,default='0')
    work_progress = models.CharField(max_length=200,null=True,default='0')

    half_day_status = models.CharField(max_length=200,null=True)
    today_total_break_time = models.CharField(max_length=200,default='00:00:00')



    def __str__(self):
        return self.staff.fullname


class staff_tasks(models.Model):
    staff = models.ForeignKey(staff_registration, on_delete=models.CASCADE,null=True, blank=True)
    task_name = models.CharField(max_length=200,null=True)
    task_links = models.CharField(max_length=200,null=True)
    task_file = models.FileField(upload_to='images/', null=True, blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    task_status = models.CharField(max_length=200,default='0')
    task_progress = models.CharField(max_length=200,null=True,default='0')
    task_progress_reports = models.CharField(max_length=200,null=True,default='No Reports')

    task_cancel_report = models.TextField(null=True)


    def __str__(self):
        return self.task_name
    
class Staff_Projects(models.Model):
    staff = models.ForeignKey(staff_registration, on_delete=models.CASCADE,null=True, blank=True)
    Project_name = models.CharField(max_length=200,null=True)
    Project_links = models.CharField(max_length=200,null=True)
    Project_file = models.FileField(upload_to='images/', null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    Project_status = models.CharField(max_length=200,default='0')
    Project_progress = models.CharField(max_length=200,null=True,default='0')
    Project_progress_reports = models.CharField(max_length=200,null=True,default='No Reports')

    def __str__(self):
        return self.staff.fullname

class staffs_basics(models.Model):
    staff = models.ForeignKey(staff_registration, on_delete=models.CASCADE,null=True, blank=True)
    today = models.DateField(auto_now=False, auto_now_add=False)
    checkin_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    checkout_time = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)

    tea_time_start = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    tea_time_end = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)

    lunch_time_start = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    lunch_time_end = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)

    over_time_start = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)
    over_time_end = models.DateTimeField(auto_now=False, auto_now_add=False,null=True, blank=True)


class Staff_Project_Task_Reports(models.Model):
    which_staff = models.ForeignKey(staff_registration, on_delete=models.CASCADE,null=True, blank=True)
    which_task = models.ForeignKey(staff_tasks, on_delete=models.CASCADE,null=True, blank=True)

    report = models.CharField(max_length=255,default='0')
    report_date = models.DateField(auto_now=False, auto_now_add=False)
    report_file = models.FileField(upload_to = 'images/', null=True, blank=True)

    def __str__(self):
        return self.which_task.task_name
    
    

    
class Attendance_Day_Break(models.Model):
    staff = models.ForeignKey(staff_registration, on_delete=models.CASCADE,null=True, blank=True)
    attendance_no = models.ForeignKey(attendance, on_delete=models.CASCADE,null=True, blank=True)
    last_countodunt = models.CharField(max_length=20,default='00:00:00')
    break_start  = models.TimeField(null=True, blank=True)
    break_end  = models.TimeField(null=True, blank=True)
    total_break_time  = models.CharField(max_length=20,default='00:00:00')
    status = models.CharField(max_length=20,default='')

    









    

