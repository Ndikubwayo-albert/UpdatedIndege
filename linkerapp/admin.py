from django.contrib import admin
from .models import Employer, Jobseeker, Rfidcard, Contact


# Register your models here.
admin.site.register(Employer)
admin.site.register(Jobseeker)

admin.site.register( Rfidcard)

admin.site.register(Contact)





admin.site.site_header = 'Daily Laborers System'
