from django.contrib import admin
from .models import Jobseeker, Rfidcard, Contact, Present_worker, Employer


# Register your models here.

admin.site.register(Employer)

admin.site.register(Jobseeker)

admin.site.register(Rfidcard)
admin.site.register(Present_worker)

admin.site.register(Contact)





admin.site.site_header = 'Daily Laborers System'
