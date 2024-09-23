import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2004"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS School;")
cursor.execute("USE School;")
cursor.execute("""CREATE TABLE IF NOT EXISTS teachers(
                id INT AUTO_INCREMENT PRIMARY KEY,
               name VARCHAR(50),
                surname VARCHAR(50),
               salary INT,
               experience int,
               
               
               
               );""")