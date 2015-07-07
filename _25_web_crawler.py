__author__ = 'royalfiish'
import requests
from bs4 import BeautifulSoup
import re

links = []
# create request to webpage
response = requests.get("http://www.novoshodnensky.org")

# convert response to html
plain = response.text

# create soup object
soup = BeautifulSoup(plain, "html.parser")

# parse anchor tags
for link in soup.find_all('a'):
    href = str(link.get('href'))

    # add domain to local links
    if not re.search('http', href):
        href = "http://www.novoshodnensky.org/" + href
    # print(href)

    # collect links to array
    links.append(href)
# print(links)
