from django.db import models
from datetime import date
from django.utils import timezone

from . import forms
from account.models import CustomUser

from django.utils.translation import gettext as _
# Create your models here.


class Employer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    
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
    work_type = models. CharField(max_length = 5000)
    other_job = models.TextField(null= True)
    
    
    
    def __str__(self):
        return self.firstname +"    "+ self.lastname
    
class Rfidcard(models.Model):
    card_id = models.IntegerField(primary_key = True, )
    # date= models.DateField( _("Date"), auto_now_add=True)
    # time= models.TimeField(_("Time"), auto_now_add=True )        
    date_added = models.DateTimeField( default= timezone.now)
    
    
    def __str__(self):
        return str(self.card_id) + "       ---"
    
class Present_worker(models.Model):
    card_id = models.IntegerField(primary_key = True, )
           
    names= models.CharField(max_length= 500)
    phone = models.CharField(max_length = 50)
    age= models.CharField( max_length=50)
    gender = models.CharField(max_length = 50)
            
    work_type = models. CharField(max_length = 5000)
    location = models.TextField() 
    date_arrived= models.DateTimeField( default= timezone.now)  
    
    
 
    
    def __str__(self):
        return self.names + "       ---"
        
    
    
    
class Contact(models.Model):    
    names = models.CharField(max_length = 5000)
    phone = models.CharField( max_length = 50, primary_key= True)
    email = models.EmailField(max_length = 5000)
    location = models.CharField(max_length=500)
    message= models.TextField()
    
    def __str__(self):
        return self.names +"          ---        "+ self.email
    
    
        
       


    




