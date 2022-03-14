from django import forms
from . models import Student_Info
from django.core import validators

class My_Form(forms.ModelForm):
    class Meta:
        model = Student_Info
        fields = ['name', 'email', 'passcode']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'passcode': forms.TextInput(attrs={'class': 'form-control'}),}