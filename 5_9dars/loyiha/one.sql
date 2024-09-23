CREATE TABLE IF NOT EXISTS TICKETS (
ID INT AUTO_INCREMENT PRIMARY KEY,
FULLNAME VARCHAR(64) NOT NULL DEFAULT "DEFAULT",
PRICE FLOAT DEFAULT 0,
STATUS BOOL DEFAULT FALSE,
SEAT_NUMBER INT NOT NULL
);


delete from tickets;

drop table tickets;

insert into TICKETS (PRICE, SEAT_NUMBER) values 
    (1000000,1),
    (1000000,2),
    (1000000,3),
    (1000000,4),
    (800000,5),
    (800000,6),
    (800000,7),
    (800000,8),
    (600000,9),
    (600000,10),
    (600000,11),
    (600000,12),
    (500000,13),
    (500000,14),
    (500000,15),
    (500000,16);
