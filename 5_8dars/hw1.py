import mysql.connector
from colorama import init, Fore
from os import system

system("cls")

init(autoreset=True)

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2004"
)

kursor = db.cursor()

def createdatabase(DatabaseName : str):
    kursor.execute(f"CREATE DATABASE IF NOT EXISTS {DatabaseName};")
    print(Fore.GREEN + "* database yarratildi")

def connectdatabase(DatabaseName : str):
    kursor.execute(f"USE {DatabaseName};")
    print(Fore.GREEN + "* databasega ulandi")

def createtable():
    kursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        name varchar(50),
        surname varchar(50),
        salary int,
        experience int,
        branch varchar(50)               
    );
    """)
    print(Fore.GREEN + "* table yaratildi")

def insertdata(name : str,surname : str, salary : int, experience : int, branch : str):
    kursor.execute("insert into teachers (name, surname, salary, experience, branch) values (%s, %s, %s, %s, %s);",
    (name,surname,salary,experience,branch))
    db.commit()
    print(Fore.GREEN + "* 1ta ma'lumot qo'shildi")

createdatabase("School")
connectdatabase("School")
createtable()
insertdata(('Zachery', 'Petrichat', 228, 5, 'chilonzor'))
insertdata(('Emory', 'MacGinlay', 310, 5, 'xadra'))
insertdata(('Kaleb', 'Priest', 594, 5, 'chilonzor'))
insertdata()
insertdata()
insertdata()
insertdata()
insertdata()
insertdata()