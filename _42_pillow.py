__author__ = 'royalfiish'
from PIL import Image

img = Image.open('img1.jpg')
print(img.size)
print(img.format)

img.show()

area = (20, 20, 100, 80)
newimg = img.crop(area)

newimg.show()
