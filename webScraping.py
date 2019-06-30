# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen

link = 'https://www.bd24live.com/bangla/'

res = urlopen(link)
page_html = res.read()
res.close()
soap = BeautifulSoup(page_html, 'html.parser')

with open('bd24live.csv', 'w', encoding='utf-8') as f:
    f.write('Link' + '\n')
    for link in soap.find_all('a'):
        link_data = ''.join(str(link).split(','))
        f.write(link_data + '\n')
f.close()
