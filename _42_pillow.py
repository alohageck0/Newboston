__author__ = 'royalfiish'
from PIL import Image

img = Image.open('img1.jpg')
print(img.size)
print(img.format)
