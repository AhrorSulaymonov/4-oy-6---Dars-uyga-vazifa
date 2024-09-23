import mysql.connector

class Database():
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "2004"
        )
        self.cursor = self.db.cursor()
        self.__setup()

    def __setup(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS telegram;")
        self.cursor.execute("USE telegram;")
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts(
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100)
            );
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS messages(
                id INT AUTO_INCREMENT PRIMARY KEY,
                contact_id INT,
                message TEXT,
                FOREGIN KEY (contact_id) REFERENCES contacts(id)          
                );
        """)

    def add_contact(self, contact_name : str):
        self.cursor.execute("INSERT INTO contacts (name)",(contact_name))
        self.db.commit()