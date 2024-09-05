from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QScrollArea, QApplication
from components import Button, Input, Label, TextArea
from database import Database

class AllPostsPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(450, 600)
        self.setWindowTitle("All Posts Page")

        self.writePostBtn = Button("Post yozish", self, 20)
        self.myPostsBtn = Button("Mening postlarim", self, 20)
        
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)

        widget = QWidget()  
        postsLayout = QVBoxLayout(widget)  

        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.writePostBtn)
        h_layout.addWidget(self.myPostsBtn)

        postsLayout.addLayout(h_layout)

        db = Database()

        posts = db.selectAllPosts()
        if len(posts) > 0:
            for i in range(len(posts)):
                post = QLineEdit(posts[i]["text"])
                post.setStyleSheet("border: 1px solid black; padding: 10px; margin: 5px;")
                postsLayout.addWidget(post)

        scrollArea.setWidget(widget)

        mainLayout = QVBoxLayout(self)
        mainLayout.addWidget(scrollArea)


