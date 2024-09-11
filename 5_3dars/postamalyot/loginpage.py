from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPalette, QBrush, QPixmap
from components import Button, Input


class LoginPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400,600)
        palette = QPalette()
        pixmap = QPixmap("Naruto.png")

        if not pixmap.isNull():
            palette.setBrush(QPalette.Background, QBrush(pixmap.scaled(self.size())))
            self.setPalette(palette)
        else:
            print("Rasmni yuklashda xatolik!")

        
        self.setWindowTitle("Register Page")
        self.usernameInput = Input(self,100,"Username...")
        self.usernameInput.setStyleSheet("""QLineEdit { 
                                            background-color: rgba(255, 255, 255, 0);
                                            font-size : 22px;
                                            border : 3px solid black; }""")
        self.passwordInput = Input(self,170,"Password...")
        self.passwordInput.setStyleSheet("""QLineEdit { 
                                            background-color: rgba(255, 255, 255, 0);
                                            font-size : 22px;
                                            border : 3px solid black; }""")

        self.loginBtn = Button("Kirish", self, 270)


# app =QApplication([])

# oyna = LoginPage()
# oyna.show()

# app.exec()