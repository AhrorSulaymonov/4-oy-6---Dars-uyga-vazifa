from PyQt5.QtWidgets import  QWidget
from components import Button, Input, Label, TextArea
from PyQt5.QtGui import QPalette, QBrush, QPixmap


class AddPostPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 500)
        palette = QPalette()
        pixmap = QPixmap("Naruto.png")

        if not pixmap.isNull():
            palette.setBrush(QPalette.Background, QBrush(pixmap.scaled(self.size())))
            self.setPalette(palette)
        else:
            print("Rasmni yuklashda xatolik!")

        self.setWindowTitle("Add Post Page")
        self.label = Label("Post yozish", self, 50)
        self.PostTextArea = TextArea(self,110)
        self.AddBtn = Button("Add", self, 320)

