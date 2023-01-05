from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from . import models


class UserRegisterForm(UserCreationForm):
    role = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['role']