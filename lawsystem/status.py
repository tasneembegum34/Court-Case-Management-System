from os import stat
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytesseract as tess
import re,time, urllib
import requests
from bs4 import BeautifulSoup
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
print(res)
num=res[0]
print(num)

element=driver.find_element(By.XPATH,"//input[contains(@id,'captcha')]").send_keys(str(num))

driver.find_element(By.XPATH,"//input[contains(@id,'searchbtn')]").click()

try:
    myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'historyform')))
    print("Page is ready!")
    status=driver.find_elements(By.XPATH,"//form[contains(@class,'historyform')]")
    print(status)
    for i in status:
        print(i.text)
    print("========")
    

    """response=requests.get(url)
    soup=BeautifulSoup(response.text,'html.parser')
    data_array=soup.find(id="caseHistoryDiv")
    print(data_array)"""
except TimeoutException:
    print("Loading took too much time!")
driver.close()