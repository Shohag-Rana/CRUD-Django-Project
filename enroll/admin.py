from django.contrib import admin
from . models import Student_Info

# Register your models here.
@admin.register(Student_Info)
class StudentModel(admin.ModelAdmin):
    list_display = ['name', 'email', 'passcode']