from PyQt5.QtWidgets import QPushButton, QLineEdit, QTextEdit, QWidget

class LineInPut(QLineEdit):
    def __init__(self, text, oyna : QWidget):
        super().__init__(oyna)
        self.setFixedSize(200,50)
        self.setStyleSheet("""
            font-size: 23px;
            color: #2D3F4B;
        """)
        self.setPlaceholderText(text)

class Button(QPushButton):
    def __init__(self, text, oyna : QWidget):
        super().__init__(oyna)
        self.setFixedSize(100,30)
        self.setText(text)
        


