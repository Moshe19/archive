-- New script in localhost.
-- Date: Sep 19, 2023
-- Time: 8:58:48 PM
# 1. Создайте представление с произвольным SELECT-запросом из прошлых уроков [CREATE VIEW]

SELECT
	COUNT(*) AS cnt,
	u.id 
FROM users AS u
JOIN friend_requests  AS fr ON (
	u.id = fr.target_user_id OR u.id = fr.initiator_user_id  
)
WHERE fr.status = 'approved'
GROUP BY u.id 
ORDER BY cnt DESC;

CREATE OR REPLACE VIEW friend_amount AS
SELECT
	COUNT(*) AS cnt,
	u.id 
FROM users AS u
JOIN friend_requests  AS fr ON (
	u.id = fr.target_user_id OR u.id = fr.initiator_user_id  
)
WHERE fr.status = 'approved'
GROUP BY u.id 
ORDER BY cnt DESC;

# 2. Выведите данные, используя написанное представление [SELECT]

SELECT * FROM friend_amount;

# 3. Удалите представление [DROP VIEW]

DROP VIEW friend_amount;

/* 4. * Сколько новостей (записей в таблице media) у каждого 
пользователя? Вывести поля: news_count (количество новостей), 
user_id (номер пользователя), user_email (email пользователя). 
Попробовать решить с помощью CTE или с помощью обычного JOIN. */

SELECT 
	count(*),
	user_id,
	email
FROM media AS m
JOIN users u ON u.id = m.user_id 
GROUP BY user_id 
