SELECT * FROM mobl_telephon.mobil_telephon;
SELECT product_name, manufakturer, price FROM mobil_telephon WHERE product_count > 2;
SELECT * FROM mobil_telephon WHERE manufakturer = 'Samsung';
SELECT * FROM mobil_telephon WHERE product_name LIKE '%iPhone%';
SELECT * FROM mobil_telephon WHERE product_name REGEXP 'Samsung';
SELECT * FROM mobil_telephon WHERE product_name regexp '[0-9]';
SELECT * FROM mobil_telephon WHERE product_name regexp '9';