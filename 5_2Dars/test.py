from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from os import system
from time import sleep

system("cls")


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bu mening 3-dasturim")
        # self.setFixedSize(400, 500)
        self.resize(400, 400)

        self.ismLabel = QLabel("Aziz mors qani?", self)
        self.ismLabel.setStyleSheet("""
            font-size: 24px;
            color: green;
        """)
        self.ismLabel.adjustSize()
        self.ismLabel.move((self.width() - self.ismLabel.width()) // 2, 100)

        self.btn = QPushButton("Close", self)
        self.btn.setStyleSheet("""
            font-size: 22px;
            color: white;
            background-color: #75c2d1;
        """)
        self.btn.resize(150, 40)
        self.btn.move((self.width() - self.btn.width()) // 2, 170)

        self.btn.clicked.connect(self.bosildi)

        self.show()


    def bosildi(self):
        msgBox = QMessageBox(self)
        msgBox.setWindowTitle("So'rov")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText("Chiqishni xohlaysizmi?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        retval = msgBox.exec()

        if retval == QMessageBox.Yes:
            print("Yes bosildi")
            self.close()
        elif retval == QMessageBox.No:
            print("No bosildi")


app = QApplication([])
oyna = Window()

app.exec()
