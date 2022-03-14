from django.db import models

# Create your models here.
class Student_Info(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    passcode = models.CharField(max_length=100)
    # image = models.ImageField(upload_to= 'enroll/images', default= "")