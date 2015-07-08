__author__ = 'royalfiish'

import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source = requests.get(url).text
    soup = BeautifulSoup(source)

# http://www.govorimpro.us/