from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pickle
from bs4 import BeautifulSoup
import requests
import random
import json
# driver = webdriver.Chrome()
options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled', False) # убирает флаг в браузере, который говорит о том что скрапит программа
options.set_preference('dom.webnotifications.enabled', False) # убирает всплывающие уведомления
options.set_preference('media.volume_scale', '0.0') # убирает звук
options.set_preference('general.useragent.override', 'example :)') # изменение user агента
# options.headless = True # запуск браузера в фоновом режиме
# options.add_argument("--headless")

driver = webdriver.Firefox(options=options)
# url = 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search'
# driver.get(url)
# time.sleep(5)
# soup = BeautifulSoup(driver.page_source, 'html.parser')

# table = soup.find

# получение прокси

# def get_proxy():
#     response = requests.get('https://www.proxyscrape.com/')
#     if 'json' in response.headers.get('Content-Type'):
#         data = response.json()
#     else:
#         print('Response content is not in JSON format.')
#         data = 'spam'   
#     proxy = random.choice(data['results'])['ip'] + ':' + data['results'][0]['port']
#     return proxy

# def scrape_website(proxy):
#     response = requests.get(url, proxies={'http': proxy, 'https': proxy})
#     soup = BeautifulSoup(response.text, "html.parser")
#     data = []
#     for row in soup.find_all('tr'):
#         data.append([cell.text for cell in row.find_all('td')])
#     return data

# if __name__== '__main__':
#     proxy = get_proxy()
#     data = scrape_website(proxy)
#     print(data)
