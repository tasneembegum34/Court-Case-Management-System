import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'E:\SHAREit\tasneemfiles\tesseract.exe'
from PIL import Image
import re
img=Image.open('captcha.png')
text=tess.image_to_string(img)
print(text)
temp=re.findall(r'\d+',text)
res=list(map(int,temp))
num=res[0]
print(num)

"""url="https://services.ecourts.gov.in/ecourtindia_v6/#"
    pageSource = driver.page_source
    response=requests.get(url)
    soup=BeautifulSoup(pageSource,'html.parser')
    data_array=soup.find(id="caseHistoryDiv")
    #print(data_array)"""