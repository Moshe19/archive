-- New script in localhost.
-- Date: Sep 14, 2023
-- Time: 3:43:00 PM

# 1. Подсчитать количество групп (сообществ), в которые вступил каждый пользователь.

SELECT user_id, COUNT(*)
FROM vk.users_communities
JOIN vk.messages ON id = community_id 
GROUP BY user_id 

# 2. Подсчитать количество пользователей в каждом сообществе.

SELECT name, COUNT(user_id)
FROM vk.communities 
JOIN vk.users_communities ON community_id = id
GROUP BY name 

/* 3. Пусть задан некоторый пользователь. Из всех пользователей соц. сети найдите человека,
 который больше всех общался с выбранным пользователем (написал ему сообщений).*/

SELECT 
	u.id, 
	u.firstname, 
	u.lastname
FROM vk.messages AS m
INNER JOIN vk.users AS u ON u.id=m.from_user_id
WHERE m.to_user_id = '1'
GROUP BY m.from_user_id
ORDER BY m.from_user_id DESC 
LIMIT 1;

#  4. Подсчитать общее количество лайков, которые получили пользователи младше 18 лет

SELECT  COUNT(l.id)
FROM vk.likes l 
JOIN vk.media m ON m.id = media_id 
JOIN vk.profiles p ON p.user_id = m.user_id 
WHERE TIMESTAMPDIFF(YEAR, p.birthday, NOW()) < '18';

# 5. Определить кто больше поставил лайков (всего): мужчины или женщины.

SELECT gender, COUNT(l.id)
FROM vk.likes l 
JOIN vk.profiles p ON p.user_id  = l.user_id 
GROUP BY gender
	


	



