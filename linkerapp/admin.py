from django.contrib import admin
from .models import Category

# Register your models here.
admin.site.register(Category)

admin.site.site_header = 'Daily Laborers System'
