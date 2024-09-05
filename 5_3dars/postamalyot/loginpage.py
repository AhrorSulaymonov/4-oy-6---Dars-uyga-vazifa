from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication
from components import Button, Input


class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setFixedSize(400,600)
        self.setWindowTitle("Register Page")
        self.usernameInput = Input(self,100,"Username...")
        self.passwordInput = Input(self,170,"Password...")

        self.loginBtn = Button("Kirish", self, 270)


# app =QApplication([])

# oyna = LoginPage()
# oyna.show()

# app.exec()