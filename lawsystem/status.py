from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytesseract as tess
import re
from bs4 import BeautifulSoup
from PIL import Image
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

tess.pytesseract.tesseract_cmd=r'E:\SHAREit\tasneemfiles\tesseract.exe'

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")


driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'cino')]").send_keys("MHAU030151912016")
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
driver.find_element(By.XPATH,"//input[contains(@id,'captcha')]").send_keys(str(num))
driver.find_element(By.XPATH,"//input[contains(@id,'searchbtn')]").click()

try:
    myElem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'historyform')))
    print("Page is ready!")
    status=driver.find_element(By.XPATH,"//form[contains(@class,'historyform')]")
    print(status)
    #print(status.text)
    print("========")
    element=driver.find_element_by_css_selector('form.historyform')
    print(element.get_attribute('innerHtml'))
except TimeoutException:
    print("Loading took too much time!")
driver.close()