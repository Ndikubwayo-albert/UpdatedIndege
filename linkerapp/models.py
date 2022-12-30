from django.db import models

# Create your models here.


class Employer(models.Model):
    emp_id = models.AutoField(primary_key = True,)
    username = models.CharField(max_length = 5000)
    firstname = models.CharField(max_length = 5000)
    lastname = models.CharField(max_length = 5000)
    phone = models.CharField(max_length = 5000)
    email = models.EmailField(max_length = 5000)
    passwd = models.CharField(null=True, max_length = 5000)
    
    def __str__(self):
        return self.firstname


    




