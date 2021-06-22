#from lawsystem.client.decorators import allowed_users
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from requests.api import head
from .models import clientAccounts, sectionNoDetails
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytesseract as tess
import re,time
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Create your views here.
from .decorators import unauthenticated_user,allowed_users

user_type=""
def home(request):
    return render(request,'home.html')
 
#@login_required(login_url='/login/')
#@allowed_users(allowed_roles=['client'])
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
                messages.error(request,"One feild is incorrect")
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
  
def caseStatus(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            cnr_no=request.POST['cnr']
            if len(cnr_no)!=16:
                messages='CNR No is less than 16 digits'
                return render(request,'caseStatus.html', {'messages':messages})
            else:
                error=""
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
                    if(len(str(num))<5):
                        error="Captch Error please enter details again"
                        raise Exception(error)

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
                            #print(j.text)
                            caseDetailsArray.append(j.text)
                    caseStatus=[]
                    for i in range(1,5):
                        l=driver.find_elements_by_xpath ("//*[@class= 'table_r table  text-left']/tbody/tr["+str(i)+"]/td")
                        for j in l:
                            caseStatus.append(j.text)
                    #print(caseDetailsArray,caseStatus)
                    driver.close()    
                    return render(request,'caseStatus.html',context={'caseDetailsArray':caseDetailsArray,'caseStatus2':caseStatus})
                except Exception as e:
                    driver.close()  
                    print(e)
                    print("Loading took too much time!")
                    return render(request,'caseStatus.html',error)
        else:
            return render(request,'caseStatus.html')
    else:
        return redirect('login')