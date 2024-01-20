from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    list_filter = [ 'name',]
    search_fields = ['name', 'email', 'phone',]
   

