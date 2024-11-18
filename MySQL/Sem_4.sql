-- New script in localhost.
-- Date: Sep 11, 2023
-- Time: 10:22:40 PM
# 1. Написать скрипт, возвращающий список имен (только firstname) пользователей без повторений в алфавитном порядке. [ORDER BY]

SELECT DISTINCT firstname
FROM vk.users
ORDER BY firstname ASC;

# 2. Выведите количество мужчин старше 35 лет [COUNT].

SELECT COUNT(*)
FROM profiles
WHERE gender = 'm'
	AND (birthday  + INTERVAL 35 YEAR) > NOW();  
	
# 3. Сколько заявок в друзья в каждом статусе? (таблица friend_requests) [GROUP BY]

SELECT status, COUNT(*)
FROM vk.friend_requests
GROUP BY status;

# 4. * Выведите номер пользователя, который отправил больше всех заявок в друзья (таблица friend_requests) [LIMIT].

SELECT initiator_user_id, COUNT(*) count_applications
FROM vk.friend_requests
GROUP BY initiator_user_id 
ORDER BY count_applications DESC 
LIMIT 1;

# 5. Выведите названия и номера групп, имена которых состоят из 5 символов [LIKE].

SELECT id, name
FROM vk.communities
WHERE name LIKE '_____';
