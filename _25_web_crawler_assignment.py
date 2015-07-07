__author__ = 'royalfiish'
import requests
from bs4 import BeautifulSoup
import re

links = []
# create request to webpage
response = requests.get("https://www.thenewboston.com/forum/topic.php?id=1610")

# convert response to html
plain = response.text

# create soup object
soup = BeautifulSoup(plain, "html.parser")

# get text from text area
code = ''
for link in soup.find_all('code'):
    code = link.text
    break
print(code)

code_arr = code.split(r' ')
for i in code_arr:
    print(i)