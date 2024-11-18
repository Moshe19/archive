DROP DATABASE IF EXISTS vk;
CREATE DATABASE vk;
USE vk;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    firstname VARCHAR(50),
    lastname VARCHAR(50) COMMENT 'Фамиль', -- COMMENT на случай, если имя неочевидное
    email VARCHAR(120) UNIQUE,
 	password_hash VARCHAR(100), -- 123456 => vzx;clvgkajrpo9udfxvsldkrn24l5456345t
	phone BIGINT UNSIGNED UNIQUE, 
	
    INDEX users_firstname_lastname_idx(firstname, lastname)
) COMMENT 'юзеры';

DROP TABLE IF EXISTS `profiles`;
CREATE TABLE `profiles` (
	user_id BIGINT UNSIGNED NOT NULL UNIQUE,
    gender CHAR(1),
    birthday DATE,
	photo_id BIGINT UNSIGNED NULL,
    created_at DATETIME DEFAULT NOW(),
    hometown VARCHAR(100)
	
    -- , FOREIGN KEY (photo_id) REFERENCES media(id) -- пока рано, т.к. таблицы media еще нет
);

ALTER TABLE `profiles` ADD CONSTRAINT fk_user_id
    FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE -- (значение по умолчанию)
    ON DELETE RESTRICT; -- (значение по умолчанию)

DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
	id SERIAL, -- SERIAL = BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
	from_user_id BIGINT UNSIGNED NOT NULL,
    to_user_id BIGINT UNSIGNED NOT NULL,
    body TEXT,
    created_at DATETIME DEFAULT NOW(), -- можно будет даже не упоминать это поле при вставке

    FOREIGN KEY (from_user_id) REFERENCES users(id),
    FOREIGN KEY (to_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS friend_requests;
CREATE TABLE friend_requests (
	-- id SERIAL, -- изменили на составной ключ (initiator_user_id, target_user_id)
	initiator_user_id BIGINT UNSIGNED NOT NULL,
    target_user_id BIGINT UNSIGNED NOT NULL,
    `status` ENUM('requested', 'approved', 'declined', 'unfriended'), # DEFAULT 'requested',
    -- `status` TINYINT(1) UNSIGNED, -- в этом случае в коде хранили бы цифирный enum (0, 1, 2, 3...)
	requested_at DATETIME DEFAULT NOW(),
	updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP, -- можно будет даже не упоминать это поле при обновлении
	
    PRIMARY KEY (initiator_user_id, target_user_id),
    FOREIGN KEY (initiator_user_id) REFERENCES users(id),
    FOREIGN KEY (target_user_id) REFERENCES users(id)-- ,
    -- CHECK (initiator_user_id <> target_user_id)
);
-- чтобы пользователь сам себе не отправил запрос в друзья
-- ALTER TABLE friend_requests 
-- ADD CHECK(initiator_user_id <> target_user_id);

DROP TABLE IF EXISTS communities;
CREATE TABLE communities(
	id SERIAL,
	name VARCHAR(150),
	admin_user_id BIGINT UNSIGNED NOT NULL,
	
	INDEX communities_name_idx(name), -- индексу можно давать свое имя (communities_name_idx)
	FOREIGN KEY (admin_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS users_communities;
CREATE TABLE users_communities(
	user_id BIGINT UNSIGNED NOT NULL,
	community_id BIGINT UNSIGNED NOT NULL,
  
	PRIMARY KEY (user_id, community_id), -- чтобы не было 2 записей о пользователе и сообществе
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (community_id) REFERENCES communities(id)
);

DROP TABLE IF EXISTS media_types;
CREATE TABLE media_types(
	id SERIAL,
    name VARCHAR(255), -- записей мало, поэтому в индексе нет необходимости
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS media;
CREATE TABLE media(
	id SERIAL,
    media_type_id BIGINT UNSIGNED NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
  	body VARCHAR(255),
    filename VARCHAR(255),
    -- file BLOB,    	
    size INT,
	metadata JSON,
    created_at DATETIME DEFAULT NOW(),
    updated_at DATETIME ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (media_type_id) REFERENCES media_types(id)
);

DROP TABLE IF EXISTS likes;
CREATE TABLE likes(
	id SERIAL,
    user_id BIGINT UNSIGNED NOT NULL,
    media_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME DEFAULT NOW(),
	FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (media_id) REFERENCES media(id)
);

ALTER TABLE vk.likes 
ADD CONSTRAINT likes_fk 
FOREIGN KEY (media_id) REFERENCES vk.media(id);

ALTER TABLE vk.likes 
ADD CONSTRAINT likes_fk_1 
FOREIGN KEY (user_id) REFERENCES vk.users(id);

ALTER TABLE vk.profiles 
ADD CONSTRAINT profiles_fk_1 
FOREIGN KEY (photo_id) REFERENCES media(id);

# задание 2

DROP TABLE IF EXISTS comment;
CREATE TABLE comment (
	id SERIAL,
	user_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	created_at DATETIME DEFAULT NOW(),
	
	FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS photo_albums;
CREATE TABLE photo_albums (
	id SERIAL,
	name VARCHAR(255),
    user_id BIGINT UNSIGNED NOT NULL,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS photos;
CREATE TABLE photos (
	id SERIAL,
	album_id BIGINT UNSIGNED,
	media_id BIGINT UNSIGNED NOT NULL,
	
	FOREIGN KEY (album_id) REFERENCES photo_albums(id),
	FOREIGN KEY (media_id) REFERENCES media(id)
);

# Задание 3

INSERT INTO users 
VALUES ('1','Иванов','Иван','ivan.ivan@yandex.ru','1','89222222222'),
    ('2','Петров','Петр','petrov.petr@yandex.ru','2','89111111111'),
    ('3','Вилкова','Вера','vilkova.vera@yandex.ru','3','89000000000'),
    ('4','Сидорова','Ксения','sidorova.ksenya@yandex.ru','4','89333333333'),
    ('5','Сталин','Иосив','stalin.iosiv@yandex.ru','5','89444444444'),
    ('6','Ленин','Владимир','lenin.vladimir@yandex.ru','6','89555555555'),
    ('7','Пунин','Владимир','putin.vladimir@yandex.ru','7','89666666666'),
    ('8','Великая','Елизавета','velikay.elizaveta@yandex.ru','8','89777777777'),
    ('9','Королева','Наташа','koroleva.natasha@yandex.ru','9','89888888888'),
    ('10','Княжна','Александра','knazna.alexandra@yandex.ru','10','89999999999');

INSERT INTO profiles 
VALUES ('1','М','2001-01-11',NULL,NOW(),'Москва'),
    ('2','М','2012-02-12',NULL,NOW(),'Сочи'),
    ('3','Ж','2002-03-13',NULL,NOW(),'Калининград'),
    ('4','Ж','2022-04-14',NULL,NOW(),'Киров'),
    ('5','М','2017-05-15',NULL,NOW(),'Киев'),
    ('6','М','2004-06-16',NULL,NOW(),'Архангельск'),
    ('7','М','2006-08-27',NULL,NOW(),'Санкт-Петербург'),
    ('8','Ж','2011-08-01',NULL,NOW(),'Владивосток'),
    ('9','Ж','2017-09-05',NULL,NOW(),'Воркута'),
    ('10','Ж','2001-10-07',NULL,NOW(),'Севастополь');
   
   /*  Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = true). 
    * При необходимости предварительно добавить такое поле в таблицу profiles 
    * со значением по умолчанию = false (или 0) (ALTER TABLE + UPDATE) */
   
ALTER TABLE profiles
ADD COLUMN is_active BIT DEFAULT 1;

UPDATE profiles 
SET is_active = 0
WHERE (birthday + INTERVAL 18 YEAR) > NOW();

# Проверим
SELECT *
FROM profiles  
WHERE is_active = 0
ORDER  BY birthday;

/*5. Написать скрипт, удаляющий сообщения «из будущего» (дата позже сегодняшней) (DELETE)*/

INSERT INTO `messages`
VALUES ('1', '1','2', 'Тестовое сообщение', '2023-09-09'),
    ('2', '3','4', 'Привет из прошлого', '2001-01-01'),
    ('3', '3','4', 'Привет из будущего!', '2027-01-01');
   
DELETE FROM messages 
WHERE created_at > NOW();

# проверим

SELECT *
FROM messages m 
ORDER BY created_at DESC;