from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
import time
import pickle
from bs4 import BeautifulSoup
import requests
import random

# url = 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search&f_tolko-v-nalichii=da&page'

# UserAgent().firefox
# def get_data(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
# #     }


# def get_data_witch_selenium(url): 
    # options = webdriver.FirefoxOptions()
    # options.set_preference('dom.webdriver.enabled', False) # убирает флаг в браузере, который говорит о том что скрапит программа
    # options.set_preference('dom.webnotifications.enabled', False) # убирает всплывающие уведомления
    # options.set_preference('media.volume_scale', '0.0') # убирает звук
    # options.set_preference('general.useragent.override', UserAgent().firefox) # изменение user агента
    # # # options.headless = True # запуск браузера в фоновом режиме
    # # options.add_argument("--headless")
    # try:
    #     driver = webdriver.Firefox(options=options)
    #     driver.get(url=url)
    #     time.sleep(10)
        
    #     with open("index_selenium.html", "w", encoding="utf-8") as file:
    #         file.write(driver.page_source)
    # except Exception as ex:
    #     print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()
    # with open("index_selenium.html", encoding='utf-8') as file:
    #     src = file.read()
    # response = requests.get(url, headers={'User-Agent' : UserAgent().chrome})
    # html = response.content
    # soup = BeautifulSoup(html, "lxml")
    # cards_url = soup.find_all('div', class_= 'product-cards-layout product-cards-layout--list')

    # for name in cards_url:
    #     name = cards_url.find('a', class_ = "product-title__text").text
    #     # price = cards_url.find('span', class_ = "price__main-value").text
    #     print(f"name = {name}\n")
        
# pickle.dump(driver.get_cookies(), open(r"C:\\Users\\admin\\Desktop\\Обучение python\\PARSING 2.0", 'wb'))
# stop = driver.find_element(By.CLASS_NAME, 'page-item ng-star-inserted disabled')

# def main():
#     get_data_witch_selenium('https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search&f_tolko-v-nalichii=da&page')


# if __name__ == '__main__':
#     main()

url = 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search&f_tolko-v-nalichii=da&page'
response = requests.get(url, headers={'User-Agent' : UserAgent().chrome})
html = response.content
soup = BeautifulSoup(html, "lxml")
cards_url = soup.find_all('div', class_= 'product-cards-layout product-cards-layout--list')

for name in cards_url:
    name = cards_url.find('a', class_ = "product-title__text").text
    # price = cards_url.find('span', class_ = "price__main-value").text
    print(f"name = {name}\n")


# def download(url):
#     resp = requests.get(url, stream=True)
#     r = open(r"C:\\Users\\admin\\Desktop\\Обучение python\\PARSING 2.0\\image\\" + url.split("/")[-1], "wb")
    
#     for value in resp.iter_content(1024*1024): #позволяет пробежаться по потоку передаваемых данных
#         r.write(value)
#     r.close()

# def get_url():

#     for count in range(1, 2):
#         url = f"https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118?from=under_search&f_tolko-v-nalichii=da&page={count}"
#         response = requests.get(url, headers=headers)
#         soup = BeautifulSoup(response.text, 'lxml')
#         data = soup.find_all('div', class_ = 'plp__card-grid')
#         for i in data:
#             card_url = "https://www.mvideo.ru" + i.find('a').get('href')
#             yield card_url
    
    
# def arrey():
                
#     for card_url in get_url():
#             response = requests.get(card_url, headers=headers)
#             time.sleep(3)
#             soup = BeautifulSoup(response.text, 'lxml')
#             data = soup.find('div', class_ = 'product-card--list ng-star-inserted')
#             # url_img = "https://www.mvideo.ru" + data.find('img', class_= 'card-img-top').get('src')
#             name = data.find('a', class_= 'product-title__text').text
#             price = data.find('span', class_= 'price__main-value').text 
#             # text = data.find('p', class_= 'card-description').text
#             # download(url_img)
#             yield name, price # text, url_img