import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//input[contains(@id,'cino')]").send_keys("MHAU030151912016")
img=driver.find_element(By.XPATH,"//img[contains(@id,'captcha_image')]")
src=img.get_attribute('src')
urllib.urlretrieve(src,"captcha.png")
driver.close()