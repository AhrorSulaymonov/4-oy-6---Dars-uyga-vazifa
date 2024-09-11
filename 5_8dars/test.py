import mysql.connector
from colorama import init, Fore
from os import system

system("cls")

init(autoreset=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1029"
)

kursor = db.cursor()

def createDatabase():
    kursor.execute("CREATE DATABASE IF NOT EXISTS BFN1;")
    print(Fore.GREEN + "* Databaza yaratilindi!")


def connectDatabase():
    kursor.execute("USE BFN1;")
    print(Fore.GREEN + "* Databazaga ulandi!")


def createTable():
    kursor.execute("""
        CREATE TABLE IF NOT EXISTS GAMES (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            TITLE VARCHAR(32) NOT NULL,
            RATING FLOAT DEFAULT 0,
            DOWNLOADS_COUNT INT DEFAULT 0,
            AUTHOR_COMPANY VARCHAR(32) NOT NULL
        );
    """)
    print(Fore.GREEN + "* Table yaratilindi!")


def insertGame(title: str, rating: float, downloads_count: int, authors: str):
    kursor.execute(
        "INSERT INTO GAMES VALUES (NULL, %s, %s, %s, %s);", 
        (title, rating, downloads_count, authors)
    )
    db.commit()
    print(Fore.GREEN + "* Malumot qo'shildi!")


def selectGames():
    kursor.execute("SELECT * FROM GAMES WHERE RATING >= 4.7;")
    games = kursor.fetchall()
    
    return games


createDatabase()
connectDatabase()
createTable()

games = selectGames()

for game in games:
    print(game)

# insertGame("Assassin's Creed", 4.7, 23_000_000, "Oliver Bowden")
# insertGame("Blur", 4.9, 123_000_000, "Bizarre Creations")
