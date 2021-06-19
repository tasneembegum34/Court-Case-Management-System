import urllib
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image

def get_captcha(driver, element, path):
    # now that we have the preliminary stuff out of the way time to get that image :D
    
    location = element.location
    size = element.size
    # saves screenshot of entire page
    driver.save_screenshot(path)

    # uses PIL library to open image in memory
    image = Image.open(path)

    left = location['x']
    top = location['y'] + 140
    right = location['x'] + size['width']
    bottom = location['y'] + size['height'] + 140

    image = image.crop((left, top, right, bottom))  # defines crop points
    image.save(path, 'jpeg')  # saves new cropped image


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://services.ecourts.gov.in/ecourtindia_v6/")

driver.implicitly_wait(10)
#img = driver.find_element_by_xpath(".//*[@id='trRandom3']/td[2]/img")
driver.find_element(By.XPATH,"//input[contains(@id,'cino')]").send_keys("MHAU030151912016")
img=driver.find_element(By.XPATH,"//img[contains(@id,'captcha_image')]")
get_captcha(driver, img, "captcha.jpeg")
src=img.get_attribute('src')
print("------------------")
print(src)
print(img.text)
print("-------------")
urllib.request.urlretrieve(src, "captcha.jpg")




driver.close()