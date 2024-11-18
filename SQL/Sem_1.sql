CREATE TABLE IF NOT EXISTS db1.mobile_phones(
	id int(10),
    ProductName varchar(50),
    Manufacturer varchar(50),
    ProductCount int(10),
    Price int(10)
);
INSERT INTO db1.mobile_phones
VALUES(
   	1, 'iPhone X', 'Apple', 3, 76000),
    (2, 'iPhone 8', 'Apple', 2, 51000),
    (3, 'Galaxy S9', 'Samsung', 2, 56000),
    (4, 'Galaxy S8', 'Samsung', 1, 41000),
    (5, 'P20 Pro', 'Huawei', 5, 36000
);

     