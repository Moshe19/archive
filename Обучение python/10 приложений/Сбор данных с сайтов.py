# import requests
# from bs4 import BeautifulSoup

# # url = 'https://quotes.toscrape.com/'
# # response = requests.get(url)
# # soup = BeautifulSoup(response.text, "lxml")
# # quotes = soup.find_all('span', class_='text')
# # authors = soup.find_all('small', class_='author')
# # tags = soup.find_all('div', class_='tags')

# # for i in range(0, len(quotes)):
# #     print(quotes[i].text)
# #     print('--' + authors[i].text)
# #     tagsforquote = tags[i].find_all('a', class_='tag')
# #     for tagforquote in tagsforquote:
# #         print(tagforquote.text)
# #     print('\n')


# url = 'https://scrapingclub.com/exercise/list_basic/?page=1.'
# parms = {'page' : 1}
# pages = 2
# n = 1

# while parms['page'] >= pages:
#     response = requests.get(url, params=parms)
#     soup = BeautifulSoup(response.text, "lxml")
#     items = soup.find_all('div', class_='grid grid-cols-1 gap-4 sm:grid-cols-3')

#     for n, i in enumerate(items, start=1):
#         itemsName = i.find('h4').text.strip()
#         itemsPrice = i.find('h5').text
#         print(f'{n}: {itemsName} за {itemsPrice}')

#     last_page_num = int(soup.find_all('a')[-2].text)
#     pages = last_page_num if pages < last_page_num else pages
#     parms['page'] += 1


import requests
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
params = {'page': 1}
# задаем число больше номера первой страницы, для старта цикла
pages = 2
n = 1

while params['page'] <= pages:
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for n, i in enumerate(items, start=n):
        itemName = i.find('h4', class_='card-title').text.strip()
        itemPrice = i.find('h5').text
        print(f'{n}:  {itemPrice} за {itemName}')

    # [-2] предпоследнее значение, потому что последнее "Next"
    last_page_num = int(soup.find_all('span', class_='page')[-2].text)
    pages = last_page_num if pages < last_page_num else pages
    params['page'] += 1