from django.utils import timezone as tz
from datetime import datetime

from django.contrib.auth.models import User, auth

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from .models import Jobseeker, Contact, Rfidcard, Employer

from account.models import CustomUser

from . import forms




# Create your views here.

def index(request):
    
    if request.method == 'POST':
        names= request.POST['names']
        phone= request.POST['phone']
        email= request.POST['email']
        location= request.POST['location']
        msg= request.POST['message']
        
        if not msg:
            messages.info(request,'Write a message !' )
            return redirect('index')
            
        else:
            new_contact= Contact(names=names, phone=phone, email=email, location=location, message=msg )
            new_contact.save()
            messages.success(request,'Your Message is sent !' )
            
            return redirect('index')          
                
    context = {  }
    return render(request, 'index.html', context )


def jobseekerreg(request):
    
    min_length= 8       
    if request.method == 'POST':
        card_id= request.POST['cardid']
        first = request.POST['firstname']
        last = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        passwd = request.POST['password']
        gender=  request.POST['sex']
        dateofbirth= request.POST['birthdate']
        indegeloc= request.POST['location']
        jobtype= request.POST['jobtype']
        other= request.POST['others']
        
        if len(passwd) < min_length:
            messages.info(request,'Password entered is less than 8 Characters !' )
            return redirect('jobseekerreg') 
        
        else:
            new_jobseeker = Jobseeker(card_id= card_id, firstname=first , lastname=last , phone=phone, email=email ,
                                 gender=gender , birth_date=dateofbirth , indege_location=indegeloc, job_type=jobtype, 
                                 other_job=other, password=passwd)
            new_jobseeker.save()
            messages.success(request,'Hey  '+ first +'!,  Account is successfully Created !' )
            
                
    return render(request, 'jobseekerreg.html', )


def employerreg(request):
        
    if request.method == 'POST':
        usern = request.POST['username']
        first = request.POST['firstname']
        last = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        passwd = request.POST['password']
        
        user = CustomUser.objects.get(account_type="employer")
        
        min_length = 8
                
        if CustomUser.objects.filter(username= usern).exists():
            messages.info(request,'Username already Taken !' )
            return redirect('employerreg')
        
        elif email is not None and CustomUser.objects.filter(email=email).exists():
            messages.info(request,'Email already Taken !' )
            return redirect('employerreg')        
                
        elif len(passwd) < min_length:
            messages.info(request,'Password entered is less than 8 Characters !' )
            return redirect('employerreg')            
        
        else:                        
            new_employer= CustomUser.objects.create( username=usern, firstname=first ,lastname=last,phone=phone,
                                                       email= email,password=passwd )
            new_employer.save() 
            
            new_user= CustomUser.objects.create(username=usern, firstname=first ,lastname=last,
                                                       email= email, password=passwd )
            new_user.save()
            
            messages.success(request,'Hey  '+ first +'!,  Your Account is successfully registered !' )  
                      
            return redirect('employerlogin') 
               
    
    return render(request, 'employerreg.html', )

def signinas(request):
    return render(request, 'signinAs.html')


def agentlogin(request):    
    if request.method == 'POST':
        username = request.POST.get('user')
        passwd = request.POST.get('pass')
        
        agent = authenticate(request, username=username, password=passwd )
        
        if agent is not None:
            login(request, agent)
            return redirect('d_agent')
        else:
            messages.info(request, 'Username Or Password is incorrect !')
        
    context= {}
    return render(request, 'agentlogin.html', context)



def emplogin(request):    
    if request.method == 'POST':
        usern= request.POST.get('user')
        passwd= request.POST.get('password')              
        user = authenticate(request, username= usern, password= passwd, account_type="employer" )
        
        if user is not None:
            login(request, user)
            return redirect('d_employer')
        else:
            messages.info(request, 'Username Or Password is incorrect !')   
            
    context = {  }
    return render(request, 'employerlogin.html', context)


def logoutuser(request):
    logout(request)    
    return redirect('index')

def registeras(request):
    return render(request, 'registerAs.html')




def adashboard(request):
    
    return render(request,'a_dashboard.html')


@login_required(login_url='employerlogin')
def edashboard(request):
    
    return render(request,'e_dashboard.html')


def availableworkers(request):
    
    query1 = Rfidcard.objects.all()
    query2 = Jobseeker.objects.all() 
  
    today = datetime.now()
    context= {
        'today' : today,
         'data' : query2
        }
       
    # if  query2 == query1:
                
    #     Tapped = query1.card_id
    #     time= datetime.now()
                
    #     name= query2.firstname
    #     phone= query2.phone
    #     age= query2.birth_date
    #     work= query2.job_type 
    #     loc= query2.indege_location
    #     gender= query2.gender
        
        
    #     new_present= Present_worker(card_id= tapped, date_arrived=time, names= name, phone= phone, age= age, work_type= work, location= loc )
    #     new_present.save()
        
    #     messages.info("done")
        
    return render(request, 'Availableworkers.html', context)


def insert_card(request, cardId):
    if request.method== 'GET':
        new_card= Rfidcard( card_id= cardId)
        new_card.save()
        messages.info(request, 'Your Presence is recorded !')
        
        # a= Rfidcard.objects.get(card_id= cardId)
        # if a.exists():
        #     return HttpResponse('exists !')
    
                
    return HttpResponse('Registered !')   
    
    # return render(request, 'availableworkers.html', context)



def about(request):
    return render(request, 'about.html')

# def contact(request):  
                    
#     return render(request, 'index.html')

def profile(request):
    return render(request,'profile.html')







