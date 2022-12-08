import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Category


# Create your views here.

def index(request):
    participants = Category.objects.all()

    context = {
        'participant': participants
    }
    return render(request, 'index.html', context)


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


def signin(request):
    return render(request, 'createAccount.html')


def login(request):
    participants = Category.objects.all()

    context = {
        'participant': participants
    }
    return render(request, 'login.html', context)


def register(request):
    return render(request, 'register.html')
