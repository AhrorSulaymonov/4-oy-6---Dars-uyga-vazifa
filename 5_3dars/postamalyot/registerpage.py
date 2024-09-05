from PyQt5.QtWidgets import  QWidget
from components import Button, Input

class RegisterPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 500)
        self.setWindowTitle("Register Page")
        self.nameInput = Input(self,100,"Name...")
        self.surnameInput = Input(self,170,"Surname...")
        self.usernameInput = Input(self,240,"Username...")
        self.passwordInput = Input(self,310,"Password...")


        self.registerBtn = Button("Registration", self, 400)

