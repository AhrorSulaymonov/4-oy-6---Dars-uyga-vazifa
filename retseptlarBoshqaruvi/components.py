from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QLineEdit, QTextEdit

class Label(QLabel):
    def __init__(self, text, oyna : QWidget) -> None:
        super().__init__(text, oyna)


class Button(QPushButton):
    def __init__(self, text, oyna : QWidget) -> None:
        super().__init__(text, oyna)

class LineInput(QLineEdit):
    def __init__(self, text, oyna : QWidget) -> None:
        super().__init__(oyna)
        self.setPlaceholderText(text)


class TextInput(QTextEdit):
    def __init__(self, text, oyna : QWidget) -> None:
        super().__init__(oyna)
        self.setPlaceholderText(text)

