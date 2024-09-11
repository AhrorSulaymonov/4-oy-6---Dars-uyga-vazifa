create database 5_7dars;

use 5_7dars;

create table apteka (
    id int AUTO_INCREMENT PRIMARY KEY,
    nname varchar(32),
    locationn text,
    kassa varchar(32)
);

insert into apteka (nname, locationn, kassa) VALUES 
    ("Dorixona1", "Chilonzor", "kassa1"),
    ("Dorixona2", "Yunusobod", "kassa2"),
    ("Dorixona3", "Olmazor", "kassa3"),
    ("Dorixona4", "Yashnabod", "kassa4"),
    ("Dorixona5", "Sergeli", "kassa5");

create table dorilar (
    id int AUTO_INCREMENT PRIMARY KEY,
    apteka_id int,
    nname varchar(32),
    price float,
    expired_date date,
    made_date date,
    count int,
    information text
);

insert into dorilar (apteka_id, nname, price, expired_date, made_date, count, information) VALUES
    (1, "sitramon", 500, "2047-01-15", "2024-05-05",40000, "hamma kasalga davo)"),
    (NULL, "parasetamol", 1000, "2027-01-15", "2024-07-05",4000, "hamma kasalga davo)"),
    (2, "hellodos", 1500, "2025-01-15", "2024-05-05",7000, "hamma kasalga davo)"),
    (3, "bosh og'ritish un dori", 500, "2037-05-25", "2024-05-06",40000, "bosh kasalga davo)");

select
    D.*,
    A.*
from dorilar as D
LEFT JOIN apteka as A
ON D.apteka_id = A.id;

select
    D.*,
    A.*
from dorilar as D
INNER JOIN apteka as A
ON D.apteka_id = A.id;

select
    D.*,
    A.*
from dorilar as D
RIGHT JOIN apteka as A
ON D.apteka_id = A.id;

select
    D.*,
    A.*
from dorilar as D
FULL JOIN apteka as A
ON D.apteka_id = A.id;