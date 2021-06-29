from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import render
from client.models import clientAccounts
from advocate.models import advocateAccounts
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
# Create your views here.
from django.contrib.auth import authenticate,login,logout
from client.decorators import unauthenticated_user

@unauthenticated_user
def loginPage(request): 
    if request.method == "POST":
        username=request.POST["uname"]
        psw=request.POST["psw"]
        try:
            usertype=request.POST["usertype"]
            print(usertype)
            if usertype=="client":
                print(username,psw)
                user1=authenticate(request,username=username,password=psw)
                if user1 is not None :
                    print("authenticated----")
                    usercli=clientAccounts.objects.filter(username=username,password=psw).exists()
                    if usercli==True:
                        login(request,user1)
                        return render(request, 'clientHome.html')
                    else:
                        messages.error(request,"Username as  usertype 'Client' unrecongnized")
                        return render(request, 'login.html')
                else:
                    messages.error(request,"Username or Password incorrect")
                    return render(request, 'login.html')
            elif usertype=="advocate":
                user1=authenticate(request,username=username,password=psw)
                if user1 is not None:
                    usercli=advocateAccounts.objects.filter(username=username,password=psw).exists()
                    if usercli==True:
                        login(request,user1)
                        return render(request, 'advocateHome.html')
                    else:
                        messages.error(request,"Username as usertype 'Advocate' unrecongnized")
                        return render(request, 'login.html')  
                else:
                    messages.error(request,'Username or Password is Incorrect')
                    return render(request, 'login.html')   
        except Exception as e:    
            print(e)
            messages.error(request,'Usertype not selected')
            return render(request, 'login.html')
       
 
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return render(request,'home.html')

def advocateSettings(request):
    return render(request,'advocateSettings.html')


def clientSettings(request):
    print(request.user)
    userInfo=clientAccounts.objects.get(username=request.user)
    if request.method=="POST"  and 'update' in request.POST:
        print("came")
        userInfo.first_name=request.POST['first_name']
        userInfo.last_name=request.POST['last_name']
        userInfo.phno=request.POST['phoneNo']
        userInfo.email=request.POST['email']
        userInfo.save()
    if request.method=="POST"  and 'change_pw' in request.POST:
        old_pw=request.POST['old_pw']
        new_pw=request.POST['new_pw']
        confirm_pw=request.POST['confirm_pw']
        cli_user=authenticate(request,username=request.user,password=old_pw)
        if cli_user is not None:
            if new_pw==confirm_pw:
                userInfo.password=new_pw
                userInfo.save()
                print(userInfo.password)
                u=User.objects.get(username=cli_user)
                u.set_password(new_pw)
                print(u.password)
                u.save()
                messages.info(request,"password successfully changed")
                return HttpResponseRedirect("/login/")
            else: 
                messages.error(request,"password does not match")
                return render(request,'clientSettings.html',{'userInfo':userInfo})
        else:
            messages.error(request,"your old password is incorrect")
            return render(request,'clientSettings.html',{'userInfo':userInfo})

    return render(request,'clientSettings.html',{'userInfo':userInfo})

    
def show_popup_once_processor(request):
    show_popup = False
    if not request.session.get('popup_seen', False):
        request.session['popup_seen'] = True
        show_popup = True
    return { "show_popup": show_popup }

