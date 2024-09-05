from PyQt5.QtWidgets import  QWidget
from components import Button, Input, Label, TextArea

class AddPostPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 500)
        self.setWindowTitle("Add Post Page")
        self.label = Label("Post yozish", self, 50)
        self.PostTextArea = TextArea(self,110)
        self.AddBtn = Button("Add", self, 320)

