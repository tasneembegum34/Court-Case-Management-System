#from lawsystem.client.decorators import allowed_users
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import clientAccounts, sectionNoDetails
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytesseract as tess
import re
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .decorators import unauthenticated_user,allowed_users
# Create your views here.

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
            address=request.POST['address']
            try:
                validate_email(email)
                username=request.POST['username']
                password=request.POST['password']
                re_password=request.POST['re_password']
                if password==re_password:
                    user=clientAccounts.objects.create(first_name=first_name,last_name=last_name,email=email,address=address,dob=dob,username=username,password=password,age=age,gender=gender,phno=phno)
                    print("user created---------------")
                    us=User.objects.create(username=username,password=password)
                    User.save(us)
                    return redirect('/regSuccessful/')
                else:
                    messages.error(request,"Password doesn't match")
                    return render(request, 'clientRegister.html')
            except ValidationError as e:
                print(e)
                messages.error(request,"bad email, details:")
                return redirect(request,"clientRegister.html")
        except Exception as e:
            if msg:
                messages.error(request,"Password doesn't match")
                return render(request, 'clientRegister.html')
            else: 
                print(e)
                messages.error(request,"One feild is incorrect")
                return render(request, 'clientRegister.html')
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
  
def caseStatus(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            cnr_no=request.POST['cnr']
            if len(cnr_no)!=16:
                mesg='CNR Number is less than 16 digits!!!'
                messages.warning(request,mesg)
                return render(request,'caseStatus.html')# {'messages':mesg})
            else:
                error=""
                num=0
                try:
                    tess.pytesseract.tesseract_cmd=r'E:\SHAREit\tasneemfiles\tesseract.exe'

                    driver=webdriver.Chrome(ChromeDriverManager().install())
                    driver.maximize_window()
                    driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")

                    driver.implicitly_wait(10)
                    #cnrno="MHAU030151912016"
                    element=driver.find_element(By.XPATH,"//input[contains(@id,'cino')]").send_keys(cnr_no)
                    
                    img=driver.find_element(By.XPATH,"//img[contains(@id,'captcha_image')]")
                    img2=driver.find_element_by_id("captcha_image")
                    screenshot_as_bytes=img2.screenshot_as_png
                    with open('captcha.png', 'wb') as f:
                        f.write(screenshot_as_bytes)
                    img=Image.open('captcha.png')
                    text=tess.image_to_string(img)
                    temp=re.findall(r'\d+',text)
                    res=list(map(int,temp))
                    num=res[0]
                    print(str(num))
                    if(len(str(num))<5):
                        error=" Error occured please enter details again"
                        messages.warning(request,error)
                        return render(request,'caseStatus.html')# {'messages':mesg})
                        raise Exception
                    else:
                        element=driver.find_element(By.XPATH,"//input[contains(@id,'captcha')]").send_keys(str(num))

                        driver.find_element(By.XPATH,"//input[contains(@id,'searchbtn')]").click()

                
                        myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'historyform')))
                        print("Page is ready!")
                        heading=driver.find_element(By.XPATH,"//h2[contains(@id,'chHeading')]")
                        caseDetailsArray=[]
                        caseDetailsArray.append(heading.text)
                        for i in range(1,5):
                            l=driver.find_elements_by_xpath ("//*[@class= 'table  case_details_table']/tbody/tr["+str(i)+"]/td")
                            for j in l:
                                caseDetailsArray.append(j.text)
                        caseStatus=[]
                        for i in range(1,5):
                            l=driver.find_elements_by_xpath ("//*[@class= 'table_r table  text-left']/tbody/tr["+str(i)+"]/td")
                            for j in l:
                                caseStatus.append(j.text)
                        return render(request,'caseStatus.html',context={'caseDetailsArray':caseDetailsArray,'caseStatus2':caseStatus})
                except Exception as e:
                    print(e)
                    print("Loading took too much time!")
                    if(error):
                        messages.error(request,error)
                        return render(request,'caseStatus.html')
                    else:
                        msg="Loading took too much time! Please try again"
                        messages.error(request,msg)
                        return render(request,'caseStatus.html')
                finally:
                    driver.close()
                    num=0
        else:
            return render(request,'caseStatus.html')
    else:
        return redirect('login')