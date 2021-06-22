from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytesseract as tess
import re,time
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

  
def slow_typing(element,text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)
        
tess.pytesseract.tesseract_cmd=r'E:\SHAREit\tasneemfiles\tesseract.exe'

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")



driver.implicitly_wait(10)
cnr_no="MHAU030151912016"
element=driver.find_element(By.XPATH,"//input[contains(@id,'cino')]").send_keys(cnr_no)

img=driver.find_element(By.XPATH,"//img[contains(@id,'captcha_image')]")
img2=driver.find_element_by_id("captcha_image")
screenshot_as_bytes=img2.screenshot_as_png
with open('captcha.png', 'wb') as f:
    f.write(screenshot_as_bytes)

img=Image.open('captcha.png')
text=tess.image_to_string(img)
print(text)
temp=re.findall(r'\d+',text)
res=list(map(int,temp))
num=res[0]

element=driver.find_element(By.XPATH,"//input[contains(@id,'captcha')]").send_keys(str(num))

driver.find_element(By.XPATH,"//input[contains(@id,'searchbtn')]").click()

try:
    myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'historyform')))
    print("Page is ready!")
    heading=driver.find_element(By.XPATH,"//h2[contains(@id,'chHeading')]")
    caseDetailsArray=[]
    caseDetailsArray.append(heading.text)
    print(heading.text)
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
    print(caseDetailsArray,caseStatus)
    
    
except Exception as e:
    print(e)
    print("Loading took too much time!")
driver.close()