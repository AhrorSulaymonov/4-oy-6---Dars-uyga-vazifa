from PyQt5.QtWidgets import QWidget, QLineEdit, QLabel, QTextEdit, QPushButton


class Label(QLabel):
    def __init__(self, text : str, oyna : QWidget):
        super().__init__(oyna)
        self.setText(text)
        self.setStyleSheet("""
            font-size: 30px;
            color: #7A7A7A;
        """)
class Input(QLineEdit):
    def __init__(self, oyna : QWidget):
        super().__init__(oyna)
        self.setFixedWidth(149)
        self.setStyleSheet("""
            font-size: 23px;
            color: #7A7A7A;
        """)
class InfoInput(QTextEdit):
    def __init__(self,oyna : QWidget):
        super().__init__(oyna)
        self.setFixedSize(200,150)
        self.setStyleSheet("""
            font-size: 23px;
            color: #7A7A7A;
        """)
class Btn(QPushButton):
    def __init__(self, text : str, oyna : QWidget):
        super().__init__(oyna)
        self.setText(text)
        self.setFixedSize(100,30)
        self.setStyleSheet("""
            font-size: 23px;
            color: #7A7A7A;
        """)
