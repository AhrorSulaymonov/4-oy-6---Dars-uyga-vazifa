from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QLabel

from database import database

class tableui(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(800, 500)
        self.move(400, 200)
        

        self.idLabel = QLabel(self)
        self.idLabel.setText("id")
        self.idLabel.setStyleSheet("""
            font-size: 26px;
            color: blue;
        """)
        self.idLabel.adjustSize()
        self.idLabel.move(70, 70)
        
        self.idInput = QLineEdit(self)
        self.idInput.move(70, 100)



app = QApplication([])

oyna = tableui()

oyna.show()

app.exec()