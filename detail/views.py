from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from .models import Rank, CourseDetails, Student, StudentDetail, Profile
from .forms import NameForm,ContactForm



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def formret(request):
    StudentInfo= StudentDetail.objects.values('studentId','studentId__studentName','studentId__CourseID__courseName','rankId_id__Desc','Score')
    return render(request,'form2.html',{'StudentInfo':StudentInfo})

def getName(request):
    form=NameForm()
    return render(request,'name.html',{'form':form})

def getContact(request):
    form1=ContactForm()
    return render(request,'contact.html',{'form':form1})


