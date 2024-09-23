import mysql.connector
from os import system
system("cls")

class Database:
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "2004"
        )
        self.cursor = self.db.cursor()
        self.__setup()

    def __setup(self):
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS library;")
        self.cursor.execute("USE library")
        self.cursor.execute("""
            create table if not exists books(
            id int auto_increment primary key,
            name varchar(32),
            autor_name varchar(32),
            information text
            );
        """)
    def insert(self, name, autor_name, information):
        self.cursor.execute("""
            INSERT INTO books (name, autor_name, information)
            values (%s, %s, %s)
        """,
        (name, autor_name, information))
        self.db.commit()

    
database = Database()
