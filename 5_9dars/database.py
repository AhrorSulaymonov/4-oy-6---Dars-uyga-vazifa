import mysql.connector
from os import system

system("cls")

class Database():
    def __init__(self) -> None:
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "2004"
        )
        self.cursor = self.db.cursor()
    def createdatabase(self, DatabaseName : str):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DatabaseName};")
        self.cursor.execute(f"USE {DatabaseName};")

    def createDorilarTable(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS dorilar(
            id INT UNIQUE,
            nomi varchar(50),
            salary float
            );
        """)
    def insertDorilar(self, id : int, nomi : str, salary : float):
        self.cursor.execute("""
            INSERT INTO dorilar values (%s, %s, %s);""",
            (id, nomi, salary)
        )

database = Database()




