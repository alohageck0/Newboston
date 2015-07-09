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
    clean_list(word_list)


def clean_list(word_list):
    clean_list = []
    for word in word_list:
        symbols = "!!!@#$%^&*()_+<>?\"{}|,:./"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 0:
            clean_list.append(word)
    count_words(clean_list)


def count_words(list):
    counted = dict()
    for word in list:
        if word in counted:
            counted[word] += 1
        else:
            counted[word] = 1
    for k, v in sorted(counted.items(), key=operator.itemgetter(1), reverse=1):
        print(k, '-', v)


start('http://www.finance.yahoo.com')
