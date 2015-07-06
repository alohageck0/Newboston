__author__ = 'royalfiish'
import random
import urllib.request

def download_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_image("http://www.novoshod-uk.ru/upload/iblock/417/4175141531a373fd75af363e43f145ae.jpg")