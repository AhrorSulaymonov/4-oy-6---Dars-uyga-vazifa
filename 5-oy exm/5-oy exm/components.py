from PyQt5.QtWidgets import QWidget, QLabel,QLineEdit, QComboBox, QPushButton

class Label(QLabel):
    def __init__(self, text: str, oyna: QWidget):
        super().__init__(oyna)
        self.setText(text)
        self.setStyleSheet("""
            font-size: 36px;
            color: red;
        """)
class ComboBox(QComboBox):
    def __init__(self, oyna: QWidget):
        super().__init__(oyna)
        self.resize(300, 40)
        self.setStyleSheet("""
            font-size: 20px;
        """)
