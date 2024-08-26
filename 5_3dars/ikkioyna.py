from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QFont

class Window(QWidget):
    def __init__(self, Parent) -> None:
        super().__init__()
        self.Parent = Parent

        self.setWindowTitle("yordamchi oyna")

        self.btnortga = QPushButton("ortga",self)
        self.btnortga.clicked.connect(self.btnclick)
        self.show()
    def btnclick(self):
        self.Parent.show()
        self.close()

class Mainwindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("asosiy oyna")
        self.btnkngioyna = QPushButton("open next window", self)
        self.btnkngioyna.clicked.connect(self.btnclicknext)

        self.show()
    def btnclicknext(self):
        self.window = Window(self)
        self.window.show()
        self.hide()
app = QApplication([])

oyna = Mainwindow()
app.exec()

