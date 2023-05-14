#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

our_host = 'http://192.168.1.68/.hidden/'

unique_texts = set()
doc_number = 0

def folder_scan(url):
    global unique_texts, doc_number
    req = requests.get(url)
    text_from_site = BeautifulSoup(req.text, 'html.parser')
    for a in text_from_site.find_all('a', href=True):
        link = a['href']
        if link[:2] == '..':
            continue
        elif link[-1] == '/':
            folder_scan(url + link)
        else:
            doc_number += 1
            print('\rscanning item #%d' %  (doc_number,), end='')
            req2 = requests.get(url + link)
            if req2.text not in unique_texts:
                unique_texts.add(req2.text)
                print('\n\t' + req2.text, url + link)

if __name__ == '__main__':
    folder_scan(our_host)
