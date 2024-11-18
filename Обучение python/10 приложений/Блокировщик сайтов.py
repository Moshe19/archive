# путь к файлу hosts Windows C:\Windows\System32\drivers\etc\hosts
# НАСТРОЙКА СРеДЫe

import time
from datetime import datetime as dt

# Путь к файлу

host_path = "hosts"

# Перенаправляем на локальный хост

redirect = "127.0.0.1 "

# Список блокируемых сайтов

website_list = ["www.netflix.com","www.facebook.com"]

# Условие

while True:
    # Проверим рабочее ли время
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("Work")
        file = open(host_path, 'r+')
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " " + website + "\n")
    else:
        print("Rest")
        file = open(host_path, 'r+')
        content = file.readlines()
        # устанавливаем курсор в начало строки
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
            file.truncate()
    time.sleep(5)