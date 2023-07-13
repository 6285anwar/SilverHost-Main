from django.shortcuts import render, redirect
from admin_app .models import *
from staff_app .models import *
from datetime import datetime, timedelta, date, time
from django.utils import timezone
import pytz
from django.http import HttpResponse
from django.http import JsonResponse



def logout(request):
    request.session.flush()
    return redirect('/')


def staff_registrations(request, des_id, text, code):
    mapping = {
        'a': 'm',
        'b': 'f',
        'c': 'k',
        'd': 'n',
        'e': 'q',
        'f': 'l',
        'g': 'w',
        'h': 'p',
        'i': 't',
        'j': 's',
        'k': 'v',
        'l': 'b',
        'm': 'u',
        'n': 'y',
        'o': 'o',
        'p': 'd',
        'q': 'x',
        'r': 'i',
        's': 'z',
        't': 'a',
        'u': 'e',
        'v': 'h',
        'w': 'r',
        'x': 'c',
        'y': 'j',
        'z': 'g',
        '1': '6',
        '2': '8',
        '3': '7',
        '4': '3',
        '5': '5',
        '6': '2',
        '7': '9',
        '8': '4',
        '9': '1',
        '0': '0'
    }
    reverse_mapping = {value: key for key, value in mapping.items()}
    decoded_text = ''
    for char in code:
        if char.lower() in reverse_mapping:
            decoded_text += reverse_mapping[char.lower()]
        else:
            decoded_text += char

    if text == decoded_text:
        des = designation.objects.get(id=des_id)
        email = text+'@gmail.com'

        return render(request, 'staff/staff_registration.html', {'des': des, 'text': text, 'email': email})
    else:
        return render(request, 'staff/error.html')


def save_staff_registration(request):
    if request.method == 'POST':
        desig = request.POST['designation']
        des = designation.objects.get(id=desig)
        email = request.POST['email']

        full_name = request.POST['fullname']
        father_name = request.POST['father']
        mother_name = request.POST['mother']
        date_of_birth = request.POST['dob']
        gender = request.POST['gender']
        address = request.POST['address']
        pincode = request.POST['pincode']
        state = request.POST['state']
        district = request.POST['district']
        country = request.POST['country']
        phone_no = request.POST['mobile']
        phone_no2 = request.POST['mobile2']
        aadhar = request.POST['aadhar']
        join_date = request.POST['join_date']

        google_pay = request.POST['google_pay']
        paypal = request.POST['paypal']
        apple_pay = request.POST['apple_pay']
        bank_name = request.POST['bank_name']
        bank_account_name = request.POST['bank_account_name']
        bank_account_no = request.POST['bank_account_no']
        ifsc_code = request.POST['ifsc']
        branch_name = request.POST['branch_name']

        profile_picture = request.FILES.get('profile_pic', False)
        id_proof = request.FILES.get('id_proof', False)

        username = request.POST['username']
        password = request.POST['password']

        status = '0'

        staff = staff_registration()
        staff.designation = des
        staff.email = email
        staff.fullname = full_name
        staff.fathername = father_name
        staff.mothername = mother_name
        staff.dateofbirth = date_of_birth
        staff.gender = gender
        staff.address = address
        staff.pincode = pincode
        staff.state = state
        staff.district = district
        staff.country = country
        staff.mobile = phone_no
        staff.alternativeno = phone_no2
        staff.aadhar_no = aadhar
        staff.joiningdate = join_date
        staff.googlepay = google_pay
        staff.paypal = paypal
        staff.applepay = apple_pay
        staff.bank_name = bank_name
        staff.account_no = bank_account_no
        staff.account_name = bank_account_name
        staff.ifsc = ifsc_code
        staff.bank_branch = branch_name
        staff.photo = profile_picture
        staff.idproof = id_proof
        staff.username = username
        staff.password = password
        staff.status = status
        staff.save()

        staff.employee_id = "SH" + \
            str(staff.id).zfill(2)
        staff.save()

        des_g = des.designation
        return render(request, 'staff/staff_reg_profile.html', {'profile_picture': profile_picture, 'full_name': full_name, 'des_g': des_g, 'email': email, 'phone_no': phone_no, 'username': username, 'password': password})


def staff_navbar(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)
        return render(request, 'staff/staff_navbar.html', {'user': user})
    else:
        return redirect('/')


def staff_dashboard(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)
        user1 = staff_registration.objects.get(id=User_id)
        em = user1.email
        dlt = staff_login_otp.objects.filter(email=em)
        dlt.delete()

        if user1.attendance_status == '-1':
            today = date.today()
            if attendance.objects.filter(staff=user1).filter(date=today).exists():

                taskss = staff_tasks.objects.filter(staff=user1)
                projectes = Staff_Projects.objects.filter(staff=user1)

                projects_count = Staff_Projects.objects.filter(
                    staff=user1).count()
                projects_count_pending = Staff_Projects.objects.filter(
                    staff=user1).filter(Project_status='1').count()
                projects_count_completed = Staff_Projects.objects.filter(
                    staff=user1).filter(Project_status='100').count()

                task_count = staff_tasks.objects.filter(staff=user1).count()
                task_count_pending = staff_tasks.objects.filter(
                    staff=user1).filter(task_status='pending').count()
                task_count_completed = staff_tasks.objects.filter(
                    staff=user1).filter(task_status='completed').count()

                tasks_today = staff_tasks.objects.filter(
                    staff=user1).filter(start_date=date.today())
                tasks_end_today = staff_tasks.objects.filter(
                    staff=user1).filter(end_date=date.today())
                try:
                    checkin_timing = attendance.objects.get(
                        staff=user1, date=date.today())
                    c_time = checkin_timing.checkin_time.strftime("%H:%M:%S")

                except:
                    c_time = '00:00:00'

                try:
                    attend = attendance.objects.get(staff=user1,date = date.today())
                    breakTime = Attendance_Day_Break.objects.filter(staff = user1).filter(attendance_no = attend)
                    time_parts = attend.today_total_break_time.split(':')
                    hour = time_parts[0]
                    minute = time_parts[1]
                    second = time_parts[2]
                    return render(request, 'staff/staff_dashboard.html', {'user': user,
                                                                    'projectes': projectes,
                                                                    'taskss': taskss,
                                                                    'projects_count': projects_count,
                                                                    'projects_count_pending': projects_count_pending,
                                                                    'projects_count_completed': projects_count_completed,
                                                                    'task_count_completed': task_count_completed,
                                                                    'task_count_pending': task_count_pending,
                                                                    'task_count': task_count,
                                                                    'tasks_today': tasks_today,
                                                                    'tasks_end_today': tasks_end_today,
                                                                    'c_time': c_time,
                                                                    'breakTime':breakTime,
                                                                    'hour':hour,'minute':minute,'second':second})
                except:
                    print('HI')

                return render(request, 'staff/staff_dashboard.html', {'user': user,
                                                                      'projectes': projectes,
                                                                      'taskss': taskss,
                                                                      'projects_count': projects_count,
                                                                      'projects_count_pending': projects_count_pending,
                                                                      'projects_count_completed': projects_count_completed,
                                                                      'task_count_completed': task_count_completed,
                                                                      'task_count_pending': task_count_pending,
                                                                      'task_count': task_count, 'tasks_today': tasks_today,
                                                                      'tasks_end_today': tasks_end_today,
                                                                      'c_time': c_time,
                                                                      })
            else:
                user1.attendance_status = '0'
                user1.checkin_status = '0'
                user1.save()

                taskss = staff_tasks.objects.filter(staff=user1)
                projectes = Staff_Projects.objects.filter(staff=user1)

                projects_count = Staff_Projects.objects.filter(
                    staff=user1).count()
                projects_count_pending = Staff_Projects.objects.filter(
                    staff=user1).filter(Project_status='1').count()
                projects_count_completed = Staff_Projects.objects.filter(
                    staff=user1).filter(Project_status='100').count()

                task_count = staff_tasks.objects.filter(staff=user1).count()
                task_count_pending = staff_tasks.objects.filter(
                    staff=user1).filter(task_status='pending').count()
                task_count_completed = staff_tasks.objects.filter(
                    staff=user1).filter(task_status='completed').count()
                tasks_today = staff_tasks.objects.filter(
                    staff=user1).filter(start_date=date.today())
                tasks_end_today = staff_tasks.objects.filter(
                    staff=user1).filter(end_date=date.today())
                try:
                    checkin_timing = attendance.objects.get(
                        staff=user1, date=date.today())
                    c_time = checkin_timing.checkin_time.strftime("%H:%M:%S")

                except:
                    c_time = '00:00:00'

                try:
                    attend = attendance.objects.get(staff=user1,date = date.today())
                    breakTime = Attendance_Day_Break.objects.filter(staff = user1).filter(attendance_no = attend)
                    time_parts = attend.today_total_break_time.split(':')
                    hour = time_parts[0]
                    minute = time_parts[1]
                    second = time_parts[2]
                    return render(request, 'staff/staff_dashboard.html', {'user': user,
                                                                    'projectes': projectes,
                                                                    'taskss': taskss,
                                                                    'projects_count': projects_count,
                                                                    'projects_count_pending': projects_count_pending,
                                                                    'projects_count_completed': projects_count_completed,
                                                                    'task_count_completed': task_count_completed,
                                                                    'task_count_pending': task_count_pending,
                                                                    'task_count': task_count,
                                                                    'tasks_today': tasks_today,
                                                                    'tasks_end_today': tasks_end_today,
                                                                    'c_time': c_time,
                                                                    'breakTime':breakTime,
                                                                    'hour':hour,'minute':minute,'second':second})
                except:
                    print('HI')


                return render(request, 'staff/staff_dashboard.html', {'user': user,
                                                                      'projectes': projectes,
                                                                      'taskss': taskss,
                                                                      'projects_count': projects_count,
                                                                      'projects_count_pending': projects_count_pending,
                                                                      'projects_count_completed': projects_count_completed,
                                                                      'task_count_completed': task_count_completed,
                                                                      'task_count_pending': task_count_pending,
                                                                      'task_count': task_count, 'tasks_today': tasks_today,
                                                                      'tasks_end_today': tasks_end_today,
                                                                      'c_time': c_time,})

        taskss = staff_tasks.objects.filter(staff=user1)

        projectes = Staff_Projects.objects.filter(staff=user1)
        projects_count = Staff_Projects.objects.filter(staff=user1).count()
        projects_count_pending = Staff_Projects.objects.filter(
            staff=user1).filter(Project_status='1').count()
        projects_count_completed = Staff_Projects.objects.filter(
            staff=user1).filter(Project_status='100').count()
        task_count = staff_tasks.objects.filter(staff=user1).count()
        task_count_pending = staff_tasks.objects.filter(
            staff=user1).filter(task_status='pending').count()
        task_count_completed = staff_tasks.objects.filter(
            staff=user1).filter(task_status='completed').count()

        tasks_today = staff_tasks.objects.filter(
            staff=user1).filter(start_date=date.today())
        tasks_end_today = staff_tasks.objects.filter(
            staff=user1).filter(end_date=date.today())

        try:
            checkin_timing = attendance.objects.get(
                staff=user1, date=date.today())
            c_time = checkin_timing.checkin_time.strftime("%H:%M:%S")

        except:
            c_time = '00:00:00'


                    
        try:
            attend = attendance.objects.get(staff=user1,date = date.today())
            breakTime = Attendance_Day_Break.objects.filter(staff = user1).filter(attendance_no = attend)

            time_parts = attend.today_total_break_time.split(':')
            hour = time_parts[0]
            minute = time_parts[1]
            second = time_parts[2]
            return render(request, 'staff/staff_dashboard.html', {'user': user,
                                                              'projectes': projectes,
                                                              'taskss': taskss,
                                                              'projects_count': projects_count,
                                                              'projects_count_pending': projects_count_pending,
                                                              'projects_count_completed': projects_count_completed,
                                                              'task_count_completed': task_count_completed,
                                                              'task_count_pending': task_count_pending,
                                                              'task_count': task_count,
                                                              'tasks_today': tasks_today,
                                                              'tasks_end_today': tasks_end_today,
                                                              'c_time': c_time,
                                                              'breakTime':breakTime,
                                                              'hour':hour,'minute':minute,'second':second})
        except:
            print('HI')
            

        return render(request, 'staff/staff_dashboard.html', {'user': user,
                                                              'projectes': projectes,
                                                              'taskss': taskss,
                                                              'projects_count': projects_count,
                                                              'projects_count_pending': projects_count_pending,
                                                              'projects_count_completed': projects_count_completed,
                                                              'task_count_completed': task_count_completed,
                                                              'task_count_pending': task_count_pending,
                                                              'task_count': task_count,
                                                              'tasks_today': tasks_today,
                                                              'tasks_end_today': tasks_end_today,
                                                              'c_time': c_time,
                                                              })
    else:
        return redirect('/')











def staff_online(request, id):
    staff = staff_registration.objects.get(id=id)
    staff.attendance_status = '1'
    staff.checkin_status = '1'
    staff.save()
    return redirect('staff_dashboard')


def staff_offline(request, id):
    staff = staff_registration.objects.get(id=id)
    staff.attendance_status = '0'
    staff.checkin_status = '0'
    staff.save()
    return redirect('staff_dashboard')


def staff_attendance(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)
        attend = attendance.objects.filter(
            staff=User_id).filter(date=(datetime.today().date()))
        attendances = attendance.objects.filter(staff=User_id)

        user1 = staff_registration.objects.get(id=User_id)
        # today = date.today()
        # atten = attendance.objects.get(staff=User_id)

        # if user1.checkin_status == 'checkout':
        #     checkout_time = datetime.combine(datetime.today(), atten.checkout_time)
        #     checkin_time = datetime.combine(datetime.today(), atten.checkin_time)

        #     time_difference = checkout_time - checkin_time

        #     fullday = timedelta(hours=8, minutes=30)
        #     halfday = timedelta(hours=4)
        #     if time_difference >= fullday:
        #         atten.status = '100'
        #         atten.save()
        #     elif time_difference >= halfday:
        #         atten.status = '50'
        #         atten.save()
        #     else:
        #         atten.status = '00'
        #         atten.save()

        # main=attendances1.checkin_time
        # kolkata_timezone = pytz.timezone('Asia/Kolkata')
        # kolkata_time = main.astimezone(kolkata_timezone)
        # print(kolkata_time)

        # print(attendance.objects.get(staff=User_id).checkin_time.astimezone(pytz.timezone('Asia/Kolkata')))

        return render(request, 'staff/staff_attendance.html', {'user': user, 'attend': attend, 'attendances': attendances})
    else:
        return redirect('/')


def staff_leave(request, id):
    staff_m = staff_registration.objects.get(id=id)
    t_date = datetime.today().date()
    if attendance.objects.filter(staff=staff_m).filter(date=(datetime.today().date())):
        return redirect(staff_attendance)
    else:
        t_time = datetime.now()

        attend = attendance()
        attend.staff = staff_m
        attend.date = t_date
        attend.start_time = t_time
        attend.today_work = '-'
        attend.status = '-100'
        attend.work_report = '-'
        attend.work_progress = '-'
        attend.save()
        return redirect(staff_attendance)


def staff_first_half_attendance(request, id):
    staff_atnd = attendance.objects.get(id=id)
    if request.method == 'POST':
        todaywork = request.POST['t_w']
        staff_atnd.today_work = todaywork
        staff_atnd.work_report = '1'
        staff_atnd.save()
        return redirect(staff_attendance)


def staff_fullday_attendance(request, id):
    staff_w = attendance.objects.get(id=id)
    if request.method == 'POST':
        workreport = request.POST['w_r']
        staff_w.work_report = workreport
        staff_w.work_progress = '1'
        staff_w.save()
        return redirect(staff_attendance)


def staff_fullday_attendance1(request, id):
    staff_w = attendance.objects.get(id=id)
    if request.method == 'POST':
        workp = request.POST['w_p']
        staff_w.work_progress = workp
        staff_w.save()
        return redirect(staff_attendance)


def staff_work_report(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)

        return render(request, 'staff/staff_work_report.html', {'user': user})
    else:
        return redirect('/')


def staff_task(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)
        user1 = staff_registration.objects.get(id=User_id)
        tasks = staff_tasks.objects.filter(staff=user1)

        total = staff_tasks.objects.filter(staff=user1).count()
        ongoing_count = staff_tasks.objects.filter(
            staff=user1).filter(task_status='ongoing').count()
        completed_count = staff_tasks.objects.filter(
            staff=user1).filter(task_status='completed').count()
        cancelled_count = staff_tasks.objects.filter(
            staff=user1).filter(task_status='cancelled').count()
        postpond_count = staff_tasks.objects.filter(
            staff=user1).filter(task_status='postpond').count()
        pendign_count = staff_tasks.objects.filter(
            staff=user1).filter(task_status='pending').count()

        current_date = date.today()
        for t in tasks:
            if t.end_date < current_date and t.task_progress != '100' and t.task_progress != '-100':
                t.task_status = 'pending'
                t.save()

        return render(request, 'staff/staff_task.html', {'user': user, 'tasks': tasks, 'ongoing_count': ongoing_count, 'completed_count': completed_count, 'cancelled_count': cancelled_count, 'postpond_count': postpond_count, 'total': total, 'pendign_count': pendign_count})
    else:
        return redirect('/')


def staff_work_accept(request, id):
    s_task = staff_tasks.objects.get(id=id)
    s_task.task_progress = '1'
    s_task.task_status = 'ongoing'
    s_task.save()
    return redirect(staff_task)


def staff_task_report(request, id):
    s_task = staff_tasks.objects.get(id=id)
    if request.method == 'POST':
        task_r = request.POST['t_r']
        task_p = request.POST['t_p']
        print(task_p)
        task_links = request.POST['t_r_l']
        task_file = request.FILES.get('t_f', False)

        s_task.task_progress_reports = task_r

        if task_p == '100':
            s_task.task_progress = task_p
            s_task.task_status = 'completed'
            s_task.save()

        else:
            s_task.task_progress = task_p
            s_task.task_status = 'ongoing'
            s_task.save()
        s_task.save()

        sptr = Staff_Project_Task_Reports()
        sptr.which_task = s_task
        sptr.which_staff = s_task.staff
        sptr.report = task_r
        sptr.report_file = task_file
        sptr.report_date = date.today()
        sptr.save()

        return redirect(staff_task)


def staff_profile(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)

        return render(request, 'staff/staff_profile.html', {'user': user})
    else:
        return redirect('/')


def staff_settings(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)

        return render(request, 'staff/staff_settings.html', {'user': user})
    else:
        return redirect('/')


def staffadd_staff_task(request, id):
    if request.method == 'POST':
        task = request.POST['task']
        tasklink = request.POST['task_link']
        taskfile = request.FILES.get('task_file', False)
        start_date = request.POST['task_start_date']
        end_date = request.POST['task_end_date']

        s = staff_registration.objects.get(id=id)
        t = staff_tasks()
        t.staff = s
        t.task_name = task
        t.task_links = tasklink
        t.task_file = taskfile
        t.start_date = start_date
        t.end_date = end_date
        t.save()
    return redirect(staff_task)


def staff_task_view(request, id):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)
        user1 = staff_registration.objects.get(id=User_id)
        tasks = staff_tasks.objects.filter(id=id)
        tasks1 = staff_tasks.objects.get(id=id)

        tasksReports = Staff_Project_Task_Reports.objects.filter(
            which_staff=user1, which_task=tasks1)
        return render(request, 'staff/staff_task_view.html', {'user': user, 'tasks': tasks, 'tasksReports': tasksReports})
    else:
        return redirect('/')


# def staff_task_cancelled(request,id):
#     tasks = staff_tasks.objects.get(id=id)
#     tasks.task_status = 'cancelled'
#     tasks.task_progress = '-100'
#     tasks.save()
#     return redirect(staff_task)


def staff_task_cancelled(request,id):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        staff_is = staff_registration.objects.get(id=User_id)
        if request.method == "POST":
            reason = request.POST["myInputtext"]
            tasks = staff_tasks.objects.get(id=id)
            tasks.task_status = 'cancelled'
            tasks.task_progress = '-100'
            tasks.task_cancel_report = reason
            tasks.save()

        return redirect(staff_task)





def staff_attend_breaktimestart(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        staff_is = staff_registration.objects.get(id=User_id)

        if request.method == "POST":
            countown_stoped = request.POST["timebreak"]
            countown_stoped = countown_stoped.replace(" ", "")
            response = {"countown_stoped": countown_stoped}
            return JsonResponse(response)
    return HttpResponse("Invalid request")


def staff_attend_breaktimeend(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        staff_is = staff_registration.objects.get(id=User_id)

        staff_attend = attendance.objects.get(staff = staff_is,date = date.today())


        if request.method == "POST":
            time_end = request.POST["timeendbreak"]
            timebreak = request.POST["timebreak"]
            BreakStart = request.POST["BreakStart"]
            BreakEnd = request.POST["BreakEnd"]

            adb = Attendance_Day_Break()
            adb.staff = staff_is
            adb.attendance_no = staff_attend
            adb.last_countodunt = timebreak
            adb.break_start  = BreakStart
            adb.break_end = BreakEnd
            adb.total_break_time = time_end
            adb.save()
            
            attendance_breaks = Attendance_Day_Break.objects.filter(attendance_no=staff_attend)
            total_break_time = timedelta(hours=0, minutes=0, seconds=0)

            for i in attendance_breaks:
                time_parts = i.total_break_time.split(':')
                if len(time_parts) != 3:
                    continue  # Skip this iteration if time_parts doesn't contain 3 elements

                try:
                    break_duration = timedelta(hours=int(time_parts[0]), minutes=int(time_parts[1]), seconds=int(time_parts[2]))
                    total_break_time += break_duration
                except ValueError:
                    continue  # Skip this iteration if there's a ValueError during conversion

            staff_attend.today_total_break_time = total_break_time
            staff_attend.save()


    
            return redirect('staff_dashboard')






def satff_task_edit(request,id):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)
        user1 = staff_registration.objects.get(id=User_id)
        tasks = staff_tasks.objects.filter(id=id)
        tasks1 = staff_tasks.objects.get(id=id)
        

        return render(request, 'staff/staff_task_edit.html', {'user': user, 'tasks1': tasks1})
    else:
        return redirect('/')

def staff_task_edit_save(request,id):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        user = staff_registration.objects.filter(id=User_id)
        user1 = staff_registration.objects.get(id=User_id)
        tasks = staff_tasks.objects.get(id=id)
        if request.method == 'POST':
            task = request.POST['task']
            tasklink = request.POST['task_link']
            taskfile = request.FILES.get('task_file', False)
            start_date = request.POST['task_start_date']
            end_date = request.POST['task_end_date']

            t = staff_tasks.objects.get(id=id)

            t.task_name = task
            t.task_links = tasklink
            if taskfile == False:
                t.task_file = tasks.task_file
            else:
                t.task_file = taskfile
            if start_date == '':
                t.start_date = tasks.start_date
            else:
                t.start_date = start_date
            if end_date == '':
                t.end_date = tasks.end_date
            else:
                t.end_date = end_date
                
            t.save()
            return redirect('staff_task')

























def staff_checkin(request, id):
    staffz = staff_registration.objects.get(id=id)
    staffz.checkin_status = 'checkin'
    staffz.save()
    staff1 = attendance()
    staff1.date = datetime.today().date()
    staff1.checkin_time = datetime.now()
    staff1.staff = staffz
    staff1.save()
    return redirect(staff_dashboard)


def staff_teatime(request, id):
    staff = staff_registration.objects.get(id=id)
    staff.checkin_status = 'tea_time'
    staff.save()
    print(staff.id)
    return redirect(staff_dashboard)


def staff_lunchtime(request, id):
    staff = staff_registration.objects.get(id=id)
    staff.checkin_status = 'lunch_time'
    staff.save()
    print(staff.id)
    return redirect(staff_dashboard)


def staff_overtime(request, id):
    staff = staff_registration.objects.get(id=id)
    staff.checkin_status = 'over_time'
    staff.save()
    print(staff.id)
    return redirect(staff_dashboard)


def staff_checkout(request, id):
    staff = staff_registration.objects.get(id=id)
    staff.checkin_status = 'checkout'
    staff.attendance_status = '-1'
    staff.save()
    today = date.today()
    try:
        staff_attend = attendance.objects.get(staff=staff, date=today)
        staff_attend.checkout_time = datetime.now().time()
        staff_attend.save()

        if staff.checkin_status == 'checkout':
            checkout_time = datetime.combine(
                date.today(), staff_attend.checkout_time)
            checkin_time = datetime.combine(
                date.today(), staff_attend.checkin_time)

            time_difference = checkout_time - checkin_time

            fullday = timedelta(hours=8, minutes=30)
            halfday = timedelta(hours=4, minutes=15)
            if time_difference >= fullday:
                staff_attend.status = '100'
            elif time_difference >= halfday:
                staff_attend.status = '50'
            else:
                staff_attend.status = '00'

            staff_attend.save()
    except attendance.DoesNotExist:
        print('No attendance record found for today.')

    return redirect(staff_dashboard)


def staff_project_doing(request, id):
    print(id)
    return redirect(staff_dashboard)


def staff_task_doing(request, id):
    tas = staff_tasks.objects.get(id=id)
    staff_n = tas.staff
    s = staff_registration.objects.get(id=staff_n.id)
    s.iam_doing = tas.task_name
    s.save()
    return redirect(staff_dashboard)


def staff_clear_doing(request, id):
    s = staff_registration.objects.get(id=id)
    s.iam_doing = ''
    s.save()
    return redirect(staff_dashboard)
