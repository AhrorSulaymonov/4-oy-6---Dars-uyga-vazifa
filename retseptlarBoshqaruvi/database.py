import mysql.connector

class Database():
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "2004"
        )
        self.cursor = self.db.cursor()

    def _stamp(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS AhrorSulaymonov;")
        self.cursor.execute("USE  AhrorSulaymonov;")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS recipes(
                recipe_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                ingredients TEXT,
                instructions TEXT
            );
        """)

database = Database()


