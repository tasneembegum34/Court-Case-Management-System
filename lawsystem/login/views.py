from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from client.models import clientAccounts
from advocate.models import advocateAccounts
from django.contrib.auth.decorators import login_required
# Create your views here.

def login(request):
    if request.method == "POST":
        username=request.POST["uname"]
        psw=request.POST["psw"]
        try:
            usertype=request.POST["usertype"]
            print(usertype)
            if usertype=="client":
                print(username,psw)
                user1=clientAccounts.objects.filter(username=username,password=psw).exists()
                print(user1)
                if user1==True:
                    print('not entered')
                    return render(request, 'clientHome.html')
                else:
                    print('entered-----')
                    messages.info(request,'username or password is incorrect')
                    return render(request, 'login.html')
            elif usertype=="advocate":
                user2=advocateAccounts.objects.filter(username=username,password=psw).exists()
                if user2==True:
                    return render(request, 'advocateHome.html')
                else:
                    messages.info(request,'username or password is incorrect')
                    return render(request, 'login.html')   
        except:    
            messages.info(request,'usertype not selected')
            return render(request, 'login.html')
       
 
    return render(request, 'login.html')


def logout(request):
    return render(request,'/home/')