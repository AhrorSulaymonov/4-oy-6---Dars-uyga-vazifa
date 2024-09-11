from PyQt5.QtWidgets import  QWidget
from components import Button, Input
from PyQt5.QtGui import QPalette, QBrush, QPixmap

class RegisterPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 500)

        palette = QPalette()
        pixmap = QPixmap("Naruto.png")

        if not pixmap.isNull():
            palette.setBrush(QPalette.Background, QBrush(pixmap.scaled(self.size())))
            self.setPalette(palette)
        else:
            print("Rasmni yuklashda xatolik!")

        self.setWindowTitle("Register Page")
        self.nameInput = Input(self,100,"Name...")
        self.surnameInput = Input(self,170,"Surname...")
        self.usernameInput = Input(self,240,"Username...")
        self.passwordInput = Input(self,310,"Password...")


        self.registerBtn = Button("Registration", self, 400)

