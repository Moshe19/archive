import requests
from requests import Session
from bs4 import BeautifulSoup
from time import sleep
from api_key import API_TOKEN

headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "www.httpbin.org",
    "Referer": "https://www.httpbin.org/",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-65d3664c-757fe24c5c8680a24f9e781d"
  }

params = {"q" : "Лондон", "appid" : API_TOKEN, "units" : "metric"}

# response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=params)
# response_user = requests.get("https://www.httpbin.org/headers", headers=headers)

# # json placeholder, httpbin.org (можно посмотреть какую информацию user передает при отправке запроса)
# # сайты для проверки и тренировки запросов

# # print(response.status_code) 
# # print(response.headers)
# # print(response.text)
# # print(response_user.json())
# print(response_user.text)

# post запросы

# теги не с сайта, это пример заполнения
variable = requests.Session()
one = variable.get("https://www.httpbin.org/form/post", headers=headers)
soup = BeautifulSoup(one.text, "lxml")
token = soup.find('form').find('input').get('value')
data = {
  "csrf_token" : token,
  "custname" : "name",
  "custtel" : "525",
  "custemail" : "sobaka@gmail.com",
  "size" : "medium",
  "topping" : "bacon",
  "delivery" : "",
  "comments" : ""}
respotse_post = variable.post("https://www.httpbin.org/post", headers=headers, data=data, allow_redirects=True)
# print(respotse_post.status_code)
print(respotse_post.text)