from django.shortcuts import redirect, render
from django.contrib import messages
from django.shortcuts import render
from client.models import clientAccounts
from advocate.models import advocateAccounts
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
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
                        messages.info(request,"Username as  usertype 'Client' unrecongnized")
                        return render(request, 'login.html')
                else:
                    messages.info(request,"Username or Password incorrect")
                    return render(request, 'login.html')
            elif usertype=="advocate":
                user1=authenticate(request,username=username,password=psw)
                if user1 is not None:
                    usercli=advocateAccounts.objects.filter(username=username,password=psw).exists()
                    if usercli==True:
                        login(request,user1)
                        return render(request, 'advocateHome.html')
                    else:
                        messages.info(request,"Username as usertype 'Advocate' unrecongnized")
                        return render(request, 'login.html')  
                else:
                    messages.info(request,'Username or Password is Incorrect')
                    return render(request, 'login.html')   
        except Exception as e:    
            print(e)
            messages.info(request,'Usertype not selected')
            return render(request, 'login.html')
       
 
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    print("came+++++++++++")
    return render(request,'home.html')


"""
user1=clientAccounts.objects.filter(username=username,password=psw).exists()
                print(user1)

                if  user1==True:
                    print('not entered')
                    password=make_password(psw)
                    us=User.objects.create(username=username,password=password)
                    User.save(us)
                    return render(request, 'clientHome.html')
                else:"""