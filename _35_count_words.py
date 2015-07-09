__author__ = 'royalfiish'

import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source = requests.get(url).text
    soup = BeautifulSoup(source, "html.parser")
    for text in soup.find_all('a'):
        content = str(text.string)
        words = content.lower().split()
        for word in words:
            word_list.append(word)
            # print(word)


start('http://www.govorimpro.us/')
