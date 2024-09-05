CREAT DATABASE COMPUTER;
USE COMPUTERS;
CREATE TABLE COMPUTERS(
    id INT AUTO_INCREMENT PRIMARY KEY,
    brand VARCHAR(32),
    model VARCHAR(32),
    cpu VARCHAR(64),
    frequency float,
    ram int,
    os VARCHAR(32),
    price float
);

select * from computers order by price desc limit 1;

select frequency from computers where cpu like "%Intel%" and where price > 400 and  price < 1000;

select count(*) from computers where brand = "Apple";