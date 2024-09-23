from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from components import LineInPut, Button
class BemorLoginUI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(1000,700)
        self.loginInput = LineInPut("Login", self)
        self.passwordInput = LineInPut("Parol", self)
        self.enterBtn = Button("Enter", self)

        Layout = QVBoxLayout()
        Layout.addWidget(self.loginInput)
        Layout.addWidget(self.passwordInput)
        Layout.addWidget(self.enterBtn)

        self.container = QWidget()
        self.container.setLayout(Layout)

        
app = QApplication([])
oyna = BemorLoginUI()
oyna.show()
app.exec()




