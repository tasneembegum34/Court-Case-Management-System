from django.contrib.auth.models import User, auth
from django.shortcuts import render,redirect
from django.contrib import messages
#from django.core.checks import messages
from django.contrib.auth.models import User
from .models import advocateAccounts
from enrollmentInfo.models import EnrollmentDetails
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
# Create your views here.
user_type=""
def home(request):
    return render(request,'home.html')
 
@login_required(login_url='/login/')
def advocateHome(request):
    return render(request,'advocateHome.html')

@unauthenticated_user
def advocateRegister(request):
    if request.method=='POST':
        try:
            msg=""
            first_name=request.POST['first_name']
            first_name=first_name.upper()
            last_name=request.POST['last_name']
            last_name=last_name.upper()
            age=request.POST['age']
            dob=request.POST['dob']
            gender=request.POST['gender']
            phno=request.POST['phno']
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['password']
            re_password=request.POST['re_password']
            experience=request.POST['experience']
            expertise=request.POST['expertise']
            address=request.POST['address']
            if password==re_password:
                eno=request.POST['eno']
                eno_date=request.POST['eno_date']
                enroll=EnrollmentDetails.objects.filter(enrollment_no=eno,enrollment_date=eno_date).exists()
                print(enroll)
                if enroll is  True:
                    print("entered usercreation")
                    user=advocateAccounts.objects.create(first_name=first_name,last_name=last_name,age=age,gender=gender,dob=dob,
                    phno=phno,email=email,username=username,password=password,experience=experience,expertise=expertise,address=address)
                    us=User.objects.create(username=username,password=password)
                    User.save(us)
                    print(user)
                    print("user created---------------")
                    return redirect('/regSuccessful/')
                   
                else:
                    messages.error(request,"Incorrect Enrollment number or date")
                    return render(request, 'advocateRegister.html')
            else:
                messages.error(request,"Password doesn't match")
                return render(request, 'advocateRegister.html')
        except Exception as e:
            if msg:
                messages.error(request,"Password doesn't match")
                return render(request, 'advocateRegister.html')
            else: 
                messages.error(request,"one feild is incorrect")
                print(e)
                return render(request, 'advocateRegister.html')
    else:
        return render(request,'advocateRegister.html')

def regSuccessful(request):
    return render(request,'regSuccessful.html')
    
