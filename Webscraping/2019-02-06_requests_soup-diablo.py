#!/usr/bin/python #Linux shebang plus chmod to make executable
#------------------------------------------------------------
# FILENAME: 2019-02-06_requests_soup-diablo.py
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

url = "https://www.icy-veins.com/d3/legendary-item-salvage-guide"
result = requests.get(url)
print(result.status_code)
#print(result.text)
print(result.encoding)

soup = BeautifulSoup(result.text, 'html.parser')
samples = soup.find_all("img", attrs={'alt': re.compile(r'.+?')})
# shorten list
samples = samples[142:-1]

for item in samples:
    print(item.get('alt'))

f = open('keepers-icy.csv', 'w', newline='')
with f:
    writer = csv.writer(f)
    for counter, value in enumerate(samples):
        writer.writerow([counter+1, value.get('alt')])
