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