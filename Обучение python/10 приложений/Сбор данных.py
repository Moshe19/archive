import requests
from bs4 import BeautifulSoup
import pandas as pd
# Пустой список для хранения данных

id_list = []

# Запрашиваем URL

page = requests.get("https://efootballhub.net/ru/efootball23/search/players")

#скачиваем страницу

soup = BeautifulSoup(page.content, "html.parser")
# print(soup.prettify())

# Повторяем цикл чтобы найти все id

for ids in range(0, 736):
    all = soup.find_all("div", "player-name")[ids]
    id_list.append(all['players-table-data'])
    
# создаем блок данных, чтобы хранить данные

df = pd.DataFrame({
    "Ids":id_list
})    

df.to_csv('player_ids.csv', index=False)
print(df, "\n Success")    
# скрапим данные

# name = soup.find("div", {"class":"profile_wiki" }).text.replace("\n", "").strip()
# print(name)