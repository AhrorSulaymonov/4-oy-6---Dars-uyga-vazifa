from PyQt5.QtWidgets import QApplication, QWidget, QLabel

class MainPageUI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize,(400, 500)
        self.setWindowTitle("Bosh sahifa")
        



app = QApplication([])

oyna = MainPageUI()
oyna.show()

app.exec()