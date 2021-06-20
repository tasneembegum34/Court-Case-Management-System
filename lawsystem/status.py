import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import base64

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

with open("captcha.png", "rb") as image:
    b64string = base64.b64encode(image.read())


driver.close()