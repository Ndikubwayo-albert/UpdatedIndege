import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



# Create your views here.

def index(request):
    
    context = {
    }
    return render(request, 'index.html', )


def createaccount(request):
    
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['uphone']
        passw1 = request.POST['pass1']
        passw2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, passw1)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()
        messages.success(request, "Successfully created")

        return redirect('index.html')
    return render(request, 'createAccount.html')


def login(request):
    # participants = Category.objects.all()

    context = {
        
    }
    return render(request, 'login.html',)


def signinas(request):
    return render(request, 'signinAs.html')

def jobseekerlogin(request):
    return render(request, 'jobseekerlogin.html')

def emplogin(request):
    return render(request, 'employerlogin.html')

def registeras(request):
    return render(request, 'registerAs.html')

def jobseekerreg(request):
    return render(request, 'jobseekerreg.html')

def employerreg(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']

        # myuser = User.objects.create_user(username, email, passw1)
        # myuser.first_name = firstname
        # myuser.last_name = lastname
        
    return render(request, 'employerreg.html')

def availableworkers(request):
    return render(request, 'Availableworkers.html')

def about(request):
    return render(request, 'about.html')





