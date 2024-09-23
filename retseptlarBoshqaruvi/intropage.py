from PyQt5.QtWidgets import QWidget, QApplication
from components import Label, Button


class IntroPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(1000, 700)
        self.fullnameLabel = Label("Ahror Sulaymonv",self)
        self.fullnameLabel.move(100,400)

        self.EnterBtn = Button("Enter",self)
        self. EnterBtn.move(800, 600)

app = QApplication([])
oyna = IntroPage()
oyna.show()
app.exec()