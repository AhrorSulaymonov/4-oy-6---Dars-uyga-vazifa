CREATE DATABASE IF NOT EXISTS AhrorSulaymonov;

USE  AhrorSulaymonov;

CREATE TABLE IF NOT EXISTS recipes(
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    ingredients TEXT,
    instructions TEXT
);

INSERT INTO recipes values (NULL, "osh", "guruch, sabzi, go'sht, yog', ziravorlar", "oldin yog' keyin go'sht keyin ...");



