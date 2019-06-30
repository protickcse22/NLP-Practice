# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen

res = urlopen('https://www.priyo.com/')
sope = BeautifulSoup(res, 'lxml')
var = sope.find_all('a')
print(type(var))
print(len(var))
for link in sope.find_all('a'):
    print(link.text)

with open('priyo.csv', 'w', encoding='utf-8') as csv_file:
    csv_file.write("Link" + "\n")
    for link in sope.find_all('a'):
        csv_file.write(''.join(link.text.split(',')) + "\n")
