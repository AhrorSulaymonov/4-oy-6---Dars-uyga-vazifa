from PyQt5.QtWidgets import QApplication, QMessageBox
from mainpage import MainPage
from loginpage import LoginPage
from registerpage import RegisterPage
from addpost import AddPostPage
from myposts import MyPostsPage
from allposts import AllPostsPage

from database import Database


from os import system
system("cls")
user_id = None
class App:
    

    def __init__(self) -> None:
        self.boshSahifaOyna = MainPage()
        self.loginOyna = LoginPage()
        self.registerOyna = RegisterPage()
        self.addPostOyna = AddPostPage()
        self.myPostsOyna = MyPostsPage(user_id)
        self.hammaPostlarOyna = AllPostsPage()
        self.database = Database()


        self.boshSahifaOyna.loginBtn.clicked.connect(self.showLoginPage)
        self.boshSahifaOyna.registerBtn.clicked.connect(self.showRegisterPage)

        self.loginOyna.loginBtn.clicked.connect(self.loginFunction)

        self.registerOyna.registerBtn.clicked.connect(self.registerFunction)
        
        self.hammaPostlarOyna.myPostsBtn.clicked.connect(self.showMyPostsOyna)
        self.hammaPostlarOyna.writePostBtn.clicked.connect(self.showAddPostOyna)

        self.addPostOyna.AddBtn.clicked.connect(self.addPostFunction)



        self.boshSahifaOyna.show()

    def addPostFunction(self):
        post_text = self.addPostOyna.PostTextArea.toPlainText()
        self.database.addpost(user_id, post_text)
        self.addPostOyna.PostTextArea.setText("")
        self.addPostOyna.PostTextArea.setPlaceholderText("muvaffaqiyatli joylandi...")


    def showAddPostOyna(self):
        self.hammaPostlarOyna.close()
        self.addPostOyna.show()

    def showMyPostsOyna(self):
        self.myPostsOyna = MyPostsPage(user_id)
        self.hammaPostlarOyna.close()
        self.myPostsOyna.show()

    def registerFunction(self):
        global user_id
        name = self.registerOyna.nameInput.text()
        surname = self.registerOyna.surnameInput.text()
        username = self.registerOyna.usernameInput.text()
        password = self.registerOyna.passwordInput.text()
        
        foundUser = self.database.selectUser(username)

        if  foundUser != None:
            return self.alert("Username band!!!")
        self.database.register(name, surname, username, password)
        user_id = self.database.selectUser(username)["id"]
        self.showAllPostsPage()
    def loginFunction(self):
        global user_id
        username = self.loginOyna.usernameInput.text()
        password = self.loginOyna.passwordInput.text()

        foundUser = self.database.login(username,password)

        if not foundUser:
            return self.alert("Foydalanuvchi nomi topilmadi!")

        self.USER = foundUser
        user_id = foundUser["id"]
        self.showAllPostsPage()

    def showAllPostsPage(self):
        self.hammaPostlarOyna.show()
        self.loginOyna.close()
        self.registerOyna.close()

    def alert(self, text : str):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(text)
        msgBox.setStandardButtons(QMessageBox.Ok)
        return msgBox.exec()

    def showLoginPage(self):
        self.boshSahifaOyna.close()
        self.loginOyna.show()

    def showRegisterPage(self):
        self.boshSahifaOyna.close()
        self.registerOyna.show()


app = QApplication([])

dastur = App()

app.exec()