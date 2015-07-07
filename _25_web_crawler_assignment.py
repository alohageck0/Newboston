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
    code = str(link)
    break
arr = code.split('<br>')
mod = arr[0]
arr[0] = mod[6:]

for i in arr:
    if not re.search('trade', i):
        print(i)