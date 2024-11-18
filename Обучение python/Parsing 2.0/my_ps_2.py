from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import pickle
from bs4 import BeautifulSoup
import requests
import random

headers = {'User-Agent' : UserAgent().chrome}

data = []
page = 1
max_page = 1
url = "https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search&f_tolko-v-nalichii=da&page="
while page <= max_page:
    res = requests.get(f"{url}{page}", headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    elements = soup.find_all('div', class_='product-cards-row ng-star-inserted')
    
    for e in elements:
        data.append({
            'name' : e.find('div', class_='product-title product-title--grid').text.strip(),
            'price' : e.find('span', class_='price__main-value').text.strip().replace('&nbsp;', ' ')
        })
    
    pagination = soup.find('li', class_='page-item number-item ng-star-inserted')
    pages = [p.text.strip() for p in pagination.find('li', class_='page-item number-item ng-star-inserted')] 
    int_pages = []
    
    for p in pages:
        try:
            n = int(p)
            int_pages.append(n)
        except:
            continue
    max_page = max(int_pages)
    page += 1
    print(page, max_page)   