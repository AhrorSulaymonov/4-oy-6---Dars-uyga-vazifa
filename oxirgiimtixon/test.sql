CREATE DATABASE IF NOT EXISTS shifoxona;
USE shifoxona;
CREATE TABLE shifokorlar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ismi VARCHAR(50),
    familiyasi VARCHAR(50),
    mutaxasisligi VARCHAR(50),
    tajribasi INT,
    oyligi INT
);


insert into shifokorlar (ismi, familiyasi, mutaxasisligi, tajribasi, oyligi)
values ('Abdulla', 'Azizov', 'Trambatolog', 7, 1200);





CREATE TABLE IF NOT EXISTS bemorlar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    ismi VARCHAR(50),
    familiyasi VARCHAR(50),
    logini VARCHAR(50),
    paroli VARCHAR(50),
    kasallik_belgilari TEXT,
    joriy_shifokor_id INT 
);

CREATE TABLE IF NOT EXISTS dorilar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nomi VARCHAR(50),
    ishlabchiqarilgansanasi DATE,
    saqlash_muddati INT,
    narxi INT,
    dori_haqida TEXT
);

CREATE TABLE IF NOT EXISTS uchrashuvlar(
    id INT AUTO_INCREMENT PRIMARY KEY,
    bemor_id INT,
    shifokor_id INT,
    uchrashuv_vaqti DATETIME
);




select count(*) from shifokorlar;