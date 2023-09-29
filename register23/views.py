from django.shortcuts import render,redirect
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from .decorators import *
# Create your views here.
import requests
from .models import Member_Records
from django.conf import settings
from django.contrib import messages
import datetime
import string
import hashlib
import random
#-------------------------------
#-------------------------------
def generate_secure_password(birthdate_str, student_id):
    base_string = birthdate_str + str(student_id)
    random_suffix = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8))
    combined_string = base_string + random_suffix
    hashed_password = hashlib.sha256(combined_string.encode()).hexdigest()
    return hashed_password
#-------------------------------
_test_re = True
_exist_record = False  
_test_re1 = True
_exist_record1 = False   
#-------------------------------

def index(request):
    return render(request,'register23/index.html',{"msg":_test_re,"exist":_exist_record})

def register(requset):
    global _test_re
    global _exist_record
    _test_re = True
    _exist_record = False
   #-------------- Post form
    if requset.method == 'POST':
        #-------------
        recaptcha_response = requset.POST.get('g-recaptcha-response')
        data = {
            'secret' :settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data = data)
        result = r.json()
        if result['success']:
        #-------------
            f_name = requset.POST['f-name']
            u_number = requset.POST['u-number']
            email = requset.POST['email']
            p_number = requset.POST['p-number']
            u_major = requset.POST['u-major']
            _date = requset.POST['date']
            #-------------- code prv create    
            _hash = generate_secure_password(_date.replace("-", ""), u_number)
            #-------------- Time now 
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime(f"%Y-%m-%d %H:%M")
            #--------------
            existing_records = Member_Records.objects.filter(f_name=f_name, u_number=u_number)
            if existing_records.exists():
                _exist_record = True
                return redirect("register-records")
            else:
                new_record = Member_Records()
                new_record.f_name = f_name
                new_record.u_number = u_number
                new_record.email=email
                new_record.p_number = p_number
                new_record.code_hash=str(_hash)
                new_record.date_b = _date
                new_record.u_major = u_major
                new_record.date_created = formatted_time
                new_record.save()
            #-----------------
        else :
            _test_re = False
            return redirect("register-records")    
    #--------------
    context= {
        'f_name':f_name,
    }
    #---------------
    return render(requset,'register23/successful.html',context)

def confirm(request):
    if request.method == 'GET':
        return render(request,'register23/404.html')
    else:
        global _test_re
        global _exist_record
        _test_re = True
        _exist_record = False
        if request.method == 'POST':
            #-------------
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret' :settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify',data = data)
            result = r.json()
            if result['success']:
                #-------------
                f_name = request.POST['f-name']
                u_number = request.POST['u-number']
                email = request.POST['email']
                p_number = request.POST['p-number']
                u_major = request.POST['u-major']
                _date = request.POST['date']
                existing_records = Member_Records.objects.filter(f_name=f_name, u_number=u_number)
                if existing_records.exists():
                    _exist_record = True
                    return redirect("register-records")
            else :
                _test_re = False
                return redirect("register-records")    
     #--------------
        context= {
            'f_name':f_name,
            'u_number':u_number,
            'email' : email,
            'p_number':p_number,
            'u_major': u_major,
            'date':_date,
            "msg":_test_re,
            "exist":_exist_record,
        }
    #----------------    
        return render(request ,'register23/confirm.html',context)


#-----------------------------------------------------
@login_required(login_url='/404')
def certificate(request,pk):
    rec=Member_Records.objects.get(id=pk)
    return render(request,'register23/certificate.html',{'rec':rec})


#-----------------------------------------------------
@login_required(login_url='/404')
def dash(request):
    records = Member_Records.objects.all()
    f_name = request.GET.get('f_name')
    u_number = request.GET.get('u_number')
    if f_name != '' and f_name is not None :
        records = records.filter(f_name=f_name)

    return render(request,'register23/dash.html',{'rec':records})

#-----------------------------------------------------
@login_required(login_url='/404')
def card(request,pk):
    rec=Member_Records.objects.get(id=pk)
    return render(request,'register23/card.html',{'rec':rec})

def userlogin(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dash')
        else:
            messages.info(request,'Not exist user')
    return render(request,'register23/login.html')
#-----------------------------------------------------
@login_required(login_url='/404')
def userlogout(request):
    logout(request)
    return redirect('/khamedmohammedtaha-cnticclub')        

def page_not_found(request):
    return render(request,'register23/404.html')
   

