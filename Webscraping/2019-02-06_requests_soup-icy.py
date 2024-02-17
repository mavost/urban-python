#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2019-02-06_requests_soup-icy.py
# VERSION: 1.0 - Python 3.6
# PURPOSE:
# AUTHOR: MVS
# LAST CHANGE: 02/06/2019
#------------------------------------------------------------
''' Python 3 main - a small piece of code
'''

import requests
from bs4 import BeautifulSoup
import re
import csv

#url = "https://www.oreilly.com/free/"
diablo = "https://us.diablo3.com"
url = diablo + "/en/item/"
result = requests.get(url)
print(result.status_code)
#print(result.text)
print(result.encoding)

soup = BeautifulSoup(result.text, 'html.parser')
#samples = soup.find_all("a", attrs={'href': re.compile("^https://")})
samples = soup.find_all("a", attrs={'href': re.compile("^/en/item")})
# shorten list
samples = samples[:-9]

for link in samples:
    print(link.get('href'))

itemlist = []

#parsing legendary and set items
#original expression from notepad++
parser = re.compile('"np" class="d3-color-(?:orange|green)">(.+?)</a>(?:.+?)<span class="d3-color-(?:orange|green)">(Legendary|Set) (Helm)</span>(?:.+?)data-raw="([0-9]*?)"')
#basic word grabbing expression
parser = re.compile(r'\w+nge')


#rebuilt expression
# flags=re.DOTALL means . matches newline as well
# ?P<> denotes group match reference
parser = re.compile(r'"np" class="d3-color-(?:orange|green)">(?P<Name>.+?)</a>(?:.+?)<span class="d3-color-(?:orange|green)">(?P<Type>Legendary|Set) (?P<Item>.+?)</span>(?:.+?)data-raw="(?P<Level>[0-9]*?)"',flags=re.DOTALL)

for link in samples:
    url = diablo + link.get('href')
    print(url)
    result = requests.get(url)

    if result.status_code == 200:
        #print(result.text)
        matches = parser.finditer(result.text)
        for match in matches:
            itemlist.append(list(match.group('Name','Type','Item','Level')))
        #soup = BeautifulSoup(result.text, 'html.parser')
        #itemlist.append(soup.find_all("a", attrs={'href': re.compile("^/en/item")}))

for item in itemlist:
    item[0] = re.sub(r'&#39;',r"'",item[0])
    print(item)

f = open('items.csv', 'w', newline='')
with f:
    writer = csv.writer(f)
    for row in itemlist:
        writer.writerow(row)
