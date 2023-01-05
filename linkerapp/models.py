from django.db import models
from datetime import date
from . import forms

from django.utils.translation import gettext as _
# Create your models here.


class Employer(models.Model):
    emp_id = models.AutoField( primary_key = True,)
    username = models.CharField(max_length = 5000)
    firstname = models.CharField(max_length = 5000)
    lastname = models.CharField(max_length = 5000)
    phone = models.CharField(max_length = 5000)
    email = models.EmailField(max_length = 5000)
    password = models.CharField( null= True, max_length = 5000)
    
    def __str__(self):
        return self.firstname +"    "+ self.lastname
    

class Jobseeker(models.Model):
    card_id = models.IntegerField(primary_key = True, )
    firstname = models.CharField(max_length = 5000)
    lastname = models.CharField(max_length = 5000)
    phone = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 5000)
    gender = models.CharField(max_length = 50)
    birth_date= models.DateField(null=True)
    indege_location = models.TextField()
    job_type = models. CharField(max_length = 5000)
    other_job = models.TextField(null= True)
    password = models.CharField(max_length = 30)
    
    
    def __str__(self):
        return self.firstname +"    "+ self.lastname
    
class Rfidcard(models.Model):
    card_id = models.IntegerField(primary_key = True, )
    # date= models.DateField( _("Date"), auto_now_add=True)
    # time= models.TimeField(_("Time"), auto_now_add=True )        
    date = models.DateField(_("Date"), default=date.today,)
    
    
    def __str__(self):
        return str(self.card_id) + "       ---"
    
    
class Contact(models.Model):    
    names = models.CharField(max_length = 5000)
    phone = models.CharField( max_length = 50, primary_key= True)
    email = models.EmailField(max_length = 5000)
    location = models.CharField(max_length=500)
    message= models.TextField()
    
    def __str__(self):
        return self.email
    
    
        
       


    




