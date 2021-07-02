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
                user1=authenticate(request,username=username,password=psw)
                if user1 is not None :
                    usercli=clientAccounts.objects.filter(username=username,password=psw).exists()
                    if usercli==True:
                        login(request,user1)
                        messages.info(request,"You have Loged in successfully!! ")
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
                        messages.info(request,"You have Loged in successfully!! ")
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
    messages.info(request,'You have Logout Successfully!!')
    return render(request,'home.html')

def advocateSettings(request):
    userInfo=advocateAccounts.objects.get(username=request.user)
    if request.method=="POST"  and 'update' in request.POST:
        print("came")
        userInfo.first_name=request.POST['first_name']
        userInfo.last_name=request.POST['last_name']
        userInfo.phno=request.POST['phoneNo']
        userInfo.email=request.POST['email']
        userInfo.save()
        messages.info(request,"Profile updated Successfully")
        print(userInfo.first_name)

    if request.method=="POST"  and 'proffUpdate' in request.POST:
        userInfo.experience=request.POST['experience']
        userInfo.expertise=request.POST['expertise']
        userInfo.additionalExpertises=request.POST.getlist('additional_expertise')
        print(userInfo.additionalExpertises)
        userInfo.save()
        messages.info(request,"Proffessional Info updated Successfully")

    if request.method=="POST"  and 'change_pw' in request.POST:
        old_pw=request.POST['old_pw']
        new_pw=request.POST['new_pw']
        confirm_pw=request.POST['confirm_pw']
        cli_user=authenticate(request,username=request.user,password=old_pw)
        if cli_user is not None:
            if new_pw!=old_pw:
                if new_pw==confirm_pw:
                    userInfo.password=new_pw
                    userInfo.save()
                    u=User.objects.get(username=cli_user)
                    u.set_password(new_pw)
                    u.save()
                    messages.info(request,"Password successfully changed")
                    return HttpResponseRedirect("/login/")
                else: 
                    messages.error(request,"Error: Password does not match")
                    return render(request,'advocateSettings.html',{'userInfo':userInfo})
            else:
                messages.error(request,"Error: New password and old password are same")
                return render(request,'advocateSettings.html',{'userInfo':userInfo})
        else:
            messages.error(request,"Error: Your old password is incorrect")
            return render(request,'advocateSettings.html',{'userInfo':userInfo})

    return render(request,'advocateSettings.html',{'userInfo':userInfo})



def clientSettings(request):
    userInfo=clientAccounts.objects.get(username=request.user)
    if request.method=="POST"  and 'update' in request.POST:
        print("came")
        userInfo.first_name=request.POST['first_name']
        userInfo.last_name=request.POST['last_name']
        userInfo.phno=request.POST['phoneNo']
        userInfo.email=request.POST['email']
        userInfo.address=request.POST['address']
        userInfo.save()
    if request.method=="POST"  and 'change_pw' in request.POST:
        old_pw=request.POST['old_pw']
        new_pw=request.POST['new_pw']
        confirm_pw=request.POST['confirm_pw']
        cli_user=authenticate(request,username=request.user,password=old_pw)
        if cli_user is not None:
            if new_pw!=old_pw:
                if new_pw==confirm_pw:
                    userInfo.password=new_pw
                    userInfo.save()
                    u=User.objects.get(username=cli_user)
                    u.set_password(new_pw)
                    u.save()
                    messages.info(request,"Password successfully changed")
                    return HttpResponseRedirect("/login/")
                else: 
                    messages.error(request,"Error: Password does not match")
                    return render(request,'clientSettings.html',{'userInfo':userInfo})
            else:
                messages.error(request,"Error: New password and old password are same")
                return render(request,'advocateSettings.html',{'userInfo':userInfo})
        else:
            messages.error(request,"Error: Your old password is incorrect")
            return render(request,'clientSettings.html',{'userInfo':userInfo})

    return render(request,'clientSettings.html',{'userInfo':userInfo})

    

