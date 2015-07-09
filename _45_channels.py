__author__ = 'royalfiish'

from PIL import Image

big_image = Image.open('img2.jpg')

r, g, b = big_image.split()

new_image = Image.merge("RGB", (b, r, g))
new_image.show()