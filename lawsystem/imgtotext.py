import pytesseract as tess
tess.pytesseract.tesseract_cmd=r'E:\SHAREit\tasneemfiles\tesseract.exe'
from PIL import Image

img=Image.open('captcha.png')
text=tess.image_to_string(img)

print(text)