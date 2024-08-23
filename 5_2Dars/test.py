from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QCheckBox
from os import system
from time import sleep

system("cls")


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bu mening 3-dasturim")
        # self.setFixedSize(400, 500)
        self.resize(400, 400)

        self.savolLabel = QLabel("Mors qani?", self)
        self.savolLabel.setStyleSheet("""
            font-size: 24px;
            color: green;
        """)
        self.savolLabel.adjustSize()
        self.savolLabel.move((self.width() - self.savolLabel.width()) // 2, 50)


        self.acceptCheckBox = QCheckBox("Hammasiga roziman otib tashla", self)
        self.acceptCheckBox.setStyleSheet("""
            font-size: 22px;
        """)
        self.acceptCheckBox.adjustSize()
        self.acceptCheckBox.move(30, 100)

        
        self.btn = QPushButton("Tanlash", self)
        self.btn.setStyleSheet("""
            QPushButton {
                font-size: 22px;
                color: white;
                background-color: #75c2d1;
            }
                               
            QPushButton::hover {
                background-color: #9bc8d1;
            }
        """)
        self.btn.resize(150, 40)
        self.btn.move((self.width() - self.btn.width()) // 2, 300)

        self.btn.setEnabled(False)

        self.acceptCheckBox.toggled.connect(lambda checked: self.tanlandi(self.acceptCheckBox, checked))
        self.btn.clicked.connect(self.bosildi)

        self.show()


    def tanlandi(self, acceptCheckBox: QCheckBox, checked: bool):
        self.btn.setEnabled(checked)
        

    def bosildi(self):
        print("Bosilyapti")
        

app = QApplication([])
oyna = Window()

app.exec()
