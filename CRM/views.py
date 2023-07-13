from django.shortcuts import render,redirect
from staff_app.models import *


def crm_navbar(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        check = staff_registration.objects.get(id=User_id)
        if check.he_is_a == 'CRM_USER':
            user = staff_registration.objects.filter(id=User_id)
            return render(request,'CRM/crm_navbar.html', {'user': user})
        else:
            return redirect('/')  
    else:
        return redirect('/')

def crm_dashboard(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        check = staff_registration.objects.get(id=User_id)
        if check.he_is_a == 'CRM_USER':
            user = staff_registration.objects.filter(id=User_id)
            return render(request,'CRM/crm_dashboard.html', {'user': user})
        else:
            return redirect('/')  
    else:
        return redirect('/')


def crm_clients(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        check = staff_registration.objects.get(id=User_id)
        if check.he_is_a == 'CRM_USER':
            user = staff_registration.objects.filter(id=User_id)
            return render(request,'CRM/crm_clients.html', {'user': user})
        else:
            return redirect('/')
    else:
        return redirect('/')

    
def crm_add_client(request):
    if 'User_id' in request.session:
        if request.session.has_key('User_id'):
            User_id = request.session['User_id']
        else:
            return redirect('/')
        check = staff_registration.objects.get(id=User_id)
        if check.he_is_a == 'CRM_USER':
            user = staff_registration.objects.filter(id=User_id)
            return render(request,'CRM/crm_add_client.html', {'user': user})
        else:
            return redirect('/')
    else:
        return redirect('/')