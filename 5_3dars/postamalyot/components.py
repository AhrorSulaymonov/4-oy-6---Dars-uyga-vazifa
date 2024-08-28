from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QLineEdit, QTextEdit, QWidget

MAX_WIDTH_BUTTON = 0
MAX_WIDTH_INPUT = 0

class Button(QPushButton):
    def __init__(self, txt : str, oyna : QWidget, y : int):
        super().__init__(txt, oyna)
        global MAX_WIDTH_BUTTON
        self.setStyleSheet("""
        QPushButton {
            font-size : 22px;
            background-color : black;
            color : white;
            border-radius : 23px;   
        }
        QPushButton::hover {
            background-color : #383838;
        }
        QPushButton::pressed {
            color : #212121;
            background-color : white;
            border : 1px solid black;           
        }
        """)
        self.y = y
        self.oyna = oyna
        self.adjustSize()
        
        
        self.resize(self.width()+50 , self.height() + 20)
        self.move((oyna.width() - self.width() )// 2, y)
        if self.width() > MAX_WIDTH_BUTTON:
            MAX_WIDTH_BUTTON = self.width()
    def changeSize(self):
        global MAX_WIDTH_BUTTON
        self.resize(MAX_WIDTH_BUTTON, self.height())
        self.move((self.oyna.width() - self.width() )// 2, self.y)

class input(QLineEdit):
    def __init__(self, oyna : QWidget, y : int):
        super().__init__(oyna)

        self.oyna = oyna
        self.y = y

        self.setGeometry(50, y, oyna.width() - 100, 50)

