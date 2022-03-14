from django.shortcuts import render, HttpResponseRedirect
from . models import Student_Info
from . forms import My_Form
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home_page(request):
    if request.method == "POST":
        fm = My_Form(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = My_Form()
    my_data = Student_Info.objects.all()
    print(my_data)
    return render(request, 'enroll/home.html', {'form': fm, 'student_data': my_data})


def update_data(request, my_id):
    pi = Student_Info.objects.get(pk= my_id)
    fm = My_Form(instance= pi)
    if request.method == "POST":
        fm = My_Form(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            psw = fm.cleaned_data['passcode']
            reg = Student_Info(id= my_id, name= nm, email= em, passcode= psw)
            reg.save()
    return render(request, 'enroll/update.html',{'form': fm})


def delete_data(request, my_id):
    pi = Student_Info.objects.get(pk= my_id)
    pi.delete()
    return HttpResponseRedirect('/')