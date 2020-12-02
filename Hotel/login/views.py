from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("Success")
        else:
            messages.error(request,"Not found in database")
            return render(request,'app/login.html')
    return render(request,'app/login.html')
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['name']
        email=request.POST['email']
        password1=request.POST['password']
        password2=request.POST['re_password']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already exists')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already exists')
            else:
                messages.error(request,'User Created')
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                #return render(request,'app/register.html',{'messages':messages})

        else:
            messages.error(request, 'Password must be same')
        return render(request,'app/register.html')
    else:
        return render(request,'app/register.html')
