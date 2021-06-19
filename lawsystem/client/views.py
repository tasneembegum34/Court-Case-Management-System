#from lawsystem.client.decorators import allowed_users
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import clientAccounts, sectionNoDetails
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.db.models import Q
#import selenium
# Create your views here.
from .decorators import unauthenticated_user,allowed_users

user_type=""
def home(request):
    return render(request,'home.html')
 
@login_required(login_url='/login/')
@allowed_users(allowed_roles=['client'])
def clientHome(request):
    print("client  home")
    return render(request,'clientHome.html') 


@unauthenticated_user
def clientRegister(request):
    if request.method=='POST':
        try:
            msg=""
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            dob=request.POST['dob']
            age=request.POST['age']
            gender=request.POST['gender']
            phno=request.POST['phno']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            re_password=request.POST['re_password']
            if password==re_password:
                user=clientAccounts.objects.create(first_name=first_name,last_name=last_name,email=email,dob=dob,username=username,password=password,age=age,gender=gender,phno=phno)
                print("user created---------------")
                us=User.objects.create(username=username,password=password)
                User.save(us)
                return redirect('/regSuccessful/')
            else:
                msg="Password doesn't match"
                return redirect()
        except Exception as e:
            if msg:
                return redirect('/clientRegister/')
            else: 
                messages.error(request,"one feild is incorrect")
                print(e)
                return redirect('/clientRegister/')
    else:
        return render(request,'clientRegister.html')

def regSuccessful(request):
            return render(request,'regSuccessful.html')
def searchSection(request):
    if request.user.is_authenticated:
        print("search entered")
        if request.method=="POST":
            searched=request.POST['searched']
            sections=sectionNoDetails.objects.filter(Q(section_name__icontains=searched) | Q(section_No=searched) | Q(chapter_No=searched))
                        #'SELECT * FROM `client_sectionnodetails` WHERE section_name like CONCAT("%",searched,"%");')
            return render(request,'searchSection.html',{'sections':sections})
        else:
            return render(request,'login.html')

        
        

def hireAdvocates(request):
    if request.user.is_authenticated:
        return render(request,'project.html')
    else:
        return redirect('login')
 