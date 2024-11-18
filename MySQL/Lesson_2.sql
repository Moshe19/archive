# создание БД
CREATE DATABASE MySamplDB; 
show databases;
# подключение к БД 
use MySamplDB;
# создание таблицы
CREATE TABLE buyer
(
id INT PRIMARY KEY AUTO_INCREMENT,
date_bird DATE,
first_name VARCHAR(20),
last_name VARCHAR(20),
mobile_phone VARCHAR(20)
);
CREATE TABLE orders
(
id INT PRIMARY KEY AUTO_INCREMENT,
buyer_if INT,
amount INT,
count_order VARCHAR(45),
FOREIGN KEY (buyer_id)
REFERENCES Buyer(id)
);