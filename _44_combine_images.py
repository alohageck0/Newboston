__author__ = 'royalfiish'

from PIL import Image

small_image = Image.open('img1.jpg')
big_image = Image.open('img2.jpg')

# print(big_image.size)
# print(small_image.size[1])

a = 100
b = 500
area = (a, b, a + small_image.size[0], b + small_image.size[1])
big_image.paste(small_image, area)
big_image.show()
