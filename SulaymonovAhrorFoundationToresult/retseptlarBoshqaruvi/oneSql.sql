CREATE DATABASE IF NOT EXISTS AhrorSulaymonov;

USE  AhrorSulaymonov;

CREATE TABLE IF NOT EXISTS recipes(
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients TEXT,
    instructions TEXT
);

INSERT INTO recipes values (NULL, "osh", "guruch, sabzi, go'sht, yog', ziravorlar", "oldin yog' keyin go'sht keyin ...");


update recipes
set name = "Osh",
    ingredients = "guruch, sabzi, go'sht, yog', ziravorlar, mayiz",
    instructions = "oldin yog' keyin go'sht keyin ... ko'p narsa"
where recipe_id = 1;




Select name from recipes where ingredients like "%go'sht%";

delete from recipes where recipe_id = 5;


