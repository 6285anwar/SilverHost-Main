from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pyshorteners
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponse



from admin_app.models import *
from .models import *
from django.db.models import Sum

from staff_app.models import *
import random









def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'INVALID CREDENTIALS'})
    else:
        return render(request, 'admin_login.html')


def login_ajax(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        dlt = staff_login_otp.objects.filter(email = username)
        dlt.delete()
        random_number = random.randint(1000, 9999)

        login_otp = staff_login_otp()
        login_otp.email = username
        login_otp.otp = random_number
        login_otp.status = '0'
        login_otp.save()

        sender_email = 'anwarsadik.disk1@gmail.com'
        receiver_email = username
        password = 'ogxemcnlxvvbflhx'
        subject = 'SilverHost Registration Form'
        message = 'Hi '
        message = 'SilverHost Login OTP.\n\n'
        message += 'OTP: ' + str(random_number)

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        # try:
        #     server = smtplib.SMTP('smtp.gmail.com', 587)
        #     server.starttls()
        #     server.login(sender_email, password)
        #     text = msg.as_string()
        #     server.sendmail(sender_email, receiver_email, text)
        #     print('Email sent successfully!')
        # except Exception as e:
        #     print(f'An error occurred while sending the email: {str(e)}')
        # finally:
        #     server.quit()

        response = {'username': username}
      
        return JsonResponse(response)

    else:
       
        return render(request, 'login.html')  


def login(request):
    if request.method == 'POST':
        email = request.POST['otp_email']
        otp1 = request.POST['otp_1']
        otp2 = request.POST['otp_2']
        otp3 = request.POST['otp_3']
        otp4 = request.POST['otp_4']


        main_otp=otp1+otp2+otp3+otp4 

        if staff_registration.objects.filter(email=email,status="1"):
            if staff_login_otp.objects.filter(email=email, otp=main_otp,status="0").exists():
                user = staff_registration.objects.get(email = request.POST['otp_email'])
                
                print(user)
                # if user.he_is_a == 'CRM_USER' and user.status == '1':
                #     crm_user = staff_registration.objects.get(email = request.POST['otp_email'])
                #     request.session['CRMUser_id'] = crm_user.id 
                #     redirect_path = '/CRM/dashboard'
                #     return redirect(redirect_path)

                # elif user.he_is_a == 'DEVELOPER' and user.status == '1':
                #     request.session['User_id'] = user.id 
                #     redirect_path = '/staff_app/staff_dashboard'
                #     return redirect(redirect_path)
                # else:
                #     return redirect('/')



                # # domain = otp_email.split('@')[-1]
                # # if domain.lower() == 'silverhost.in':
                request.session['User_id'] = user.id 
                print(user,'lllllllllllllll')
                redirect_path = '/staff_app/staff_dashboard'
                print(user,'xxxxxxxxxxxxxx')
                return redirect(redirect_path)
                # # else:
                # #     return HttpResponse('Invalid Email Id')
                
        else:
            print('no logger')

        return redirect('login')


        # if staff_login_otp.objects.filter(email=email, main_otp=main_otp,status="1").exists():
        #     user = staff_registration.objects.get(email = request.POST['username'],password = request.POST['password'])
        #     request.session['User_id'] = user.id            
        #     redirect_path = '/staff_app/staff_dashboard'
        #     return redirect(redirect_path)
        # else:
        #     return render(request, 'login.html', {'error': 'INVALID CREDENTIALS'})
    else:
        return render(request, 'login.html')


def admin_navbar(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        print(admin)
        return render(request, 'admin/admin_navbar.html', {'admin': admin})
    else:
        return redirect('/')


def admin_dashboard(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)

        return render(request, 'admin/admin_dashboard.html', {'admin': admin})
    else:
        return redirect('/')


def admin_staff(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)



        desig = designation.objects.all()
        all = designation.objects.aggregate(total_count_sum=Sum('total_count'))['total_count_sum']
        staff = staff_registration.objects.all()

        for des in desig:
            staffs_des = staff_registration.objects.filter(designation=des.id).count()
            des.total_count = staffs_des
            des.save()
            
        
        return render(request, 'admin/admin_staff.html', {'admin': admin,'desig':desig,'all':all,'staff':staff})
    else:
        return redirect('/')

def admin_desig_save(request):
    if request.method == 'POST':
        desig = request.POST['designation']
        des = designation(designation = desig)
        des.save()
    return redirect(admin_staff)


def admin_project(request):
    return render(request, 'admin/admin_project.html')


def admin_create_project(request):
    return render(request, 'admin/admin_create_project.html')


def admin_staff_email_registration(request):
    shortener = pyshorteners.Shortener()
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

    if request.method == 'POST':
        fullname = request.POST['fullname']
        desig = request.POST['desig']
        email = request.POST['email']

        des = designation.objects.get(id=desig)
        designat = des.designation
        
        des_id = str(des.id)
        print(des_id)





        text = email.split("@")[0]
        encoded_text = ''
        for char in text:
            if char.lower() in mapping:
                encoded_text += mapping[char.lower()]
            else:
                encoded_text += char

        current_url =f"{request.scheme}://{request.get_host()}/"
      

        link = current_url+'staff_app/staff_registrations/'+des_id+'/'+text+'/'+encoded_text
        link_url = shortener.tinyurl.short(link)

        sender_email = 'anwarsadik.disk1@gmail.com'
        receiver_email = email
        password = 'ogxemcnlxvvbflhx'
        subject = 'SilverHost Registration Form'
        message = 'Hi '+fullname+','
        message = 'SilverHost Registartion Form Link.\n\n'
        message += 'Link: ' + link_url + '\n'

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print('Email sent successfully!')
        except Exception as e:
            print(f'An error occurred while sending the email: {str(e)}')
        finally:
            server.quit()
    return redirect(admin_staff)
 



def admin_staff_view_profile(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        staff = staff_registration.objects.get(id=id)
        return render(request, 'admin/admin_staff_view_profile.html', {'admin': admin,'staff':staff})
    else:
        return redirect('/')

def staff_activation(request,id):
    staff = staff_registration.objects.get(id=id)
    staff.status='1'
    staff.save()
    return redirect(reverse('admin_staff_view_profile', args=[id]))
def staff_deactivation(request,id):
    staff = staff_registration.objects.get(id=id)
    staff.status='-1'
    staff.save()
    return redirect(reverse('admin_staff_view_profile', args=[id]))












def admin_staff_teams(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        return render(request, 'admin/admin_staff_teams.html', {'admin': admin})
    else:
        return redirect('/')


def admin_staff_task(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        staff = staff_registration.objects.all()
        s_tasks = staff_tasks.objects.all()

        if request.method == 'POST':
            staffname = request.POST['staff_name']
            task = request.POST['task']
            tasklink = request.POST['task_link']
            taskfile = request.FILES.get('task_file', False)
            start_date = request.POST['task_start_date']

            end_date = request.POST['task_end_date']


            # print('staffname:',staffname )
            # print('task:',task )
            # print('tasklink:',tasklink )
            # print('taskfile:',taskfile )
            # print('end_date:',end_date )
            # print('end_time:',end_time )

            s=staff_registration.objects.get(id=staffname)
            t = staff_tasks()
            t.staff = s
            t.task_name = task
            t.task_links = tasklink
            t.task_file = taskfile
            t.start_date = start_date
            t.end_date = end_date
            t.save()
            



            return redirect('admin_staff_task')



        return render(request, 'admin/admin_staff_task.html', {'admin': admin,'staff':staff,'s_tasks':s_tasks})
    else:
        return redirect('/')




def admin_staff_attendance(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)

        staffs = staff_registration.objects.all()
        staff_attnds = attendance.objects.all()
    
        return render(request,'admin/admin_staff_attendance.html',{'admin': admin,'staff_attnds':staff_attnds,'staffs':staffs})
    else:
        return redirect('/')


def admin_staff_breaktimeview(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        staf = attendance.objects.get(id=id)

        breaks = Attendance_Day_Break.objects.filter(attendance_no = staf)

        return render(request,'admin/admin_staff_breaktimeview.html',{'admin': admin,'staf':staf,'breaks':breaks})
    else:
        return redirect('/')

def admin_staff_whatdoing(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        staffss = staff_registration.objects.all()
        return render(request,'admin/admin_staff_whatdoing.html',{'admin': admin,'staffss':staffss})
    else:
        return redirect('/')
