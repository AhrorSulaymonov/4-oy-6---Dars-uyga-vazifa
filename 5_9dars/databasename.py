from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QLabel, QApplication

from database import database

class databaseui(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(800, 500)
        self.move(400, 200)
        self.databaseLabel = QLabel(self)
        
        self.databaseLabel.setText("Database nomini kiriting!")
        self.databaseLabel.setStyleSheet("""
            font-size: 26px;
            color: blue;
        """)
        self.databaseLabel.adjustSize()
        self.databaseLabel.move((self.width() - self.databaseLabel.width())//2, 70)

        self.databaseNameInput = QLineEdit(self)
        self.databaseNameInput.setStyleSheet("font-size : 25px")
        self.databaseNameInput.setPlaceholderText("Database's name")
        self.databaseNameInput.adjustSize()
        self.databaseNameInput.move((self.width() - self.databaseNameInput.width())//2, 110)

        self.btn = QPushButton(self)
        self.btn.setText("click bro")
        self.btn.adjustSize()
        self.btn.move((self.width() - self.btn.width())//2, 170)
        self.btn.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if len(self.databaseNameInput.text()) == 0:
            self.databaseLabel.setStyleSheet("font-size: 26px; color: red;")
        else:
            self.databaseLabel.setStyleSheet("font-size: 26px; color: green;")
            database.createdatabase(self.databaseNameInput.text())
            database.createDorilarTable()



app = QApplication([])

oyna = databaseui()

oyna.show()

app.exec()