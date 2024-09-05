create table talabalar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    talaba_ismi varchar(32),
    talaba_kursi int,
    talaba_stipendiyasi float
);

UPDATE talabalar
set talaba_kursi = talaba_kursi + 1;
delete from talabalar
where talaba_kursi = 5;

UPDATE talabalar
SET talaba_kursi = talaba_kursi + 1;

DELETE FROM talabalar
WHERE talaba_kursi = 5;


select count(*) , talaba_kursi from talabalar 
GROUP BY talaba_kursi;

