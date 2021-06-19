import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from PIL import Image

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")


driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'cino')]").send_keys("MHAU030151912016")
img=driver.find_element(By.XPATH,"//img[contains(@id,'captcha_image')]")
img2=driver.find_element_by_id("captcha_image").screenshot_as_png("captcha.png")
src=img.get_attribute('src')
print("------------------")
print(src)
print(img.text)
print("-------------")
#urllib.request.urlretrieve(src, "captcha.jpg")

driver.close()