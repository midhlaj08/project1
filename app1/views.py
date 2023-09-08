from django.shortcuts import render
from app1.models import table_user
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request,"home.html")

def create_account(request):
    return render(request,"create_account.html")

def add_user(request):
    a=table_user()
    b=User()
    b.username=request.POST.get('username')
    a.username=request.POST.get('username')
    b.first_name=request.POST.get('firstname')
    b.last_name=request.POST.get('lastname')
    password=request.POST.get('password')
    b.set_password(password)
    a.gender=request.POST.get('gender')
    a.phone=request.POST.get('phone')
    a.email=request.POST.get('email')
    b.email=request.POST.get('email')
    a.place=request.POST.get('place')
    photo=request.FILES['photo']
    fs=FileSystemStorage()
    c=fs.save(photo.name,photo)
    d=fs.url(c)
    a.photo=d
    a.address=request.POST.get('address')
    a.save()
    b.save()
    return render(request, "home.html")

def login1(request):
    a=request.POST.get('username')
    b=request.POST.get('password')
    c=authenticate(username=a, password=b)
    if c is not None and c.is_superuser==1:
        return render(request, "admin.html")
    elif c is not None and c.is_superuser==0:
        return render(request,"user.html")
    else:
        return HttpResponse("invalid user")