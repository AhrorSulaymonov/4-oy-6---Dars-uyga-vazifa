from PyQt5.QtWidgets import  QWidget, QLabel, QScrollArea, QVBoxLayout, QApplication, QLineEdit
from components import Button, Input, Label, TextArea
from database import Database

class MyPostsPage(QWidget):
    def __init__(self, user_id) -> None:
        super().__init__()
        self.setFixedSize(400, 600)
        self.setWindowTitle("My Posts Page")
        self.label = Label("Mening postlarim",self,10)
        scrolArea = QScrollArea()
        scrolArea.setWidgetResizable(True)

        postsWidget = QWidget()
        postsLayout = QVBoxLayout(postsWidget)

        db = Database()
        
        userPosts = db.selectuserPosts(user_id)

        

        if len(userPosts) > 0:
            for i in range(len(userPosts)):
                post = QLineEdit(userPosts[i]["text"])
                post.setFixedHeight(50)
                post.setStyleSheet("border: 1px solid black; padding: 10px; margin: 5px;")
                postsLayout.addWidget(post)
            scrolArea.setWidget(postsWidget)

            mainLayout = QVBoxLayout(self)
            mainLayout.addWidget(self.label)
            mainLayout.addWidget(scrolArea)
            



# app = QApplication([])

# oyna = MyPostsPage(2)
# oyna.show()

# app.exec()

        
        
