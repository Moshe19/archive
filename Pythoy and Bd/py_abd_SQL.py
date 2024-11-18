import sqlite3
from sqlite3 import Error

# функция, которая принимает путь к БД SQlte
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print('Connection to SQLite DB successful')
    except Error as e:
        print(f"The error '{e}' occurred")
        
    return connection

connection = create_connection(r'C:\Users\admin\Desktop\MySQL\_vk_db_creation.sql')
 
# создаем подключение к БД

conn = sqlite3.connect('user_db.db')

# создаем курсор для выполнения SQL-запросов
 
cursor = conn.cursor()

# Создаем таблицу для хранения информации о пользователе

cursor.execute('''
               ''')

# сохраняем изменения
conn.commit()

# закрываем соединение

conn.close()