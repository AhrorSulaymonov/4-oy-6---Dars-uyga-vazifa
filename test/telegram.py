import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QTextEdit, QPushButton, QHBoxLayout, QMainWindow, QDialog, QLineEdit, QLabel

db = mysql.connector.connect(
    host="localhost",
    user="root", 
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


# Asosiy oyna
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Telegram Clone")

        # Kontaktlar ro'yxati
        self.contact_list = QListWidget()
        self.load_contacts()  # MySQL'dan kontaktlarni yuklash
        self.contact_list.itemClicked.connect(self.open_chat_window)

        # Kontakt qo'shish tugmasi
        self.add_contact_button = QPushButton("Kontakt qo'shish")
        self.add_contact_button.clicked.connect(self.open_add_contact_window)

        # Chat maydoni
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        # Yozish maydoni va yuborish tugmasi
        self.text_input = QTextEdit()
        self.text_input.setMaximumHeight(50)
        self.send_button = QPushButton("Yuborish")
        self.send_button.clicked.connect(self.send_message)

        # Asosiy tuzilma
        layout = QVBoxLayout()
        layout.addWidget(self.contact_list)
        layout.addWidget(self.chat_area)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.text_input)
        input_layout.addWidget(self.send_button)

        layout.addLayout(input_layout)
        layout.addWidget(self.add_contact_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def load_contacts(self):
        cursor.execute("SELECT name FROM contacts")
        contacts = cursor.fetchall()
        for contact in contacts:
            self.contact_list.addItem(contact[0])

    def open_add_contact_window(self):
        self.add_contact_window = AddContactWindow()
        self.add_contact_window.show()

    def open_chat_window(self):
        selected_contact = self.contact_list.currentItem().text()
        self.chat_window = ChatWindow(selected_contact, self)
        self.chat_window.show()

    def send_message(self):
        message = self.text_input.toPlainText()
        selected_contact = self.contact_list.currentItem().text()

        if message and selected_contact:
            # Asosiy oynada yozilgan xabar "Siz:" deb boshlansin
            self.chat_area.append(f"Siz: {message}")
            self.chat_window.receive_message(f"Siz: {message}")  # Chat oynasiga ham chiqsin
            self.text_input.clear()

            # MySQL'ga xabarni saqlash
            cursor.execute("SELECT id FROM contacts WHERE name = %s", (selected_contact,))
            contact_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO messages (contact_id, message) VALUES (%s, %s)", (contact_id, message))
            db.commit()

# Kontakt qo'shish oynasi
class AddContactWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kontakt qo'shish")

        self.name_label = QLabel("Kontakt ismi:")
        self.name_input = QLineEdit()

        self.add_button = QPushButton("Qo'shildi")
        self.add_button.clicked.connect(self.add_contact)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_contact(self):
        contact_name = self.name_input.text()

        if contact_name:
            # MySQL'ga yangi kontaktni qo'shish
            cursor.execute("INSERT INTO contacts (name) VALUES (%s)", (contact_name,))
            db.commit()

            # Asosiy oynaga yangi kontaktni qo'shish
            main_window.contact_list.addItem(contact_name)

            # Oynani yopish
            self.close()

# Ikkinchi oyna (Chat oynasi)
class ChatWindow(QDialog):
    def __init__(self, contact_name, main_window):
        super().__init__()

        self.setWindowTitle(f"Chat: {contact_name}")
        self.contact_name = contact_name
        self.main_window = main_window  # Asosiy oynani ulash

        # Chat maydoni
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        # Yozish maydoni va yuborish tugmasi
        self.text_input = QTextEdit()
        self.text_input.setMaximumHeight(50)
        self.send_button = QPushButton("Yuborish")
        self.send_button.clicked.connect(self.send_message)

        # Oynaning tuzilmasi
        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.text_input)
        input_layout.addWidget(self.send_button)

        layout.addLayout(input_layout)
        self.setLayout(layout)

    def send_message(self):
        message = self.text_input.toPlainText()
        if message:
            # Ikkinchi oynada yozilgan xabar kontakt ismi bilan chiqsin
            self.chat_area.append(f"{self.contact_name}: {message}")
            self.main_window.chat_area.append(f"{self.contact_name}: {message}")  # Asosiy oynaga xabar chiqarish
            self.text_input.clear()

            # MySQL'ga xabarni saqlash
            cursor.execute("SELECT id FROM contacts WHERE name = %s", (self.contact_name,))
            contact_id = cursor.fetchone()[0]
            cursor.execute("INSERT INTO messages (contact_id, message) VALUES (%s, %s)", (contact_id, message))
            db.commit()

    def receive_message(self, message):
        self.chat_area.append(message)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())
