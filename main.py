# Day 1
from bs4 import BeautifulSoup 
import requests
import re

URL = 'https://en.wikipedia.org/wiki/Harry_Potter'

page = requests.get(URL)

#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
regex = re.compile('^tocsection-')
content_lis = soup.find_all('li', attrs={'class': regex})
print(content_lis)



