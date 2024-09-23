import mysql.connector
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QListWidget, QHBoxLayout, QApplication

# MySQL bilan bog'lanish
db = mysql.connector.connect(
    host="localhost",
    user="root",  # User ismingni va parolingni moslashtir
    password="2004"
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS telegram;")
cursor.execute("USE telegram;")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100)
    );
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contact_id INT,
    message TEXT,
    FOREIGN KEY (contact_id) REFERENCES contacts(id)
    );
""")

