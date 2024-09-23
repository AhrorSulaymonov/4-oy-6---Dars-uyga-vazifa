from PyQt5.QtWidgets import QWidget, QApplication
from components import Label, Input, InfoInput, Btn
from database import database
from os import system
system("cls")

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        #o'lchamlarini kiritdik
        self.resize(1000,600)
        self.move(300,200)
        # ID o'zi sanaladi shunchaki  korinib turadi
        self.idSelecterLabel = Label("ID |", self)
        self.idSelecterLabel.adjustSize()
        self.idSelecterLabel.move(50,50)

        #kitob nomi , autor nomi va kitob haqida informatsiyalar yoziladi
        self.nameSelecterLabel = Label("book name |",self)
        self.nameSelecterLabel.move(110,50)
        self.nameSelecter = Input(self)
        self.nameSelecter.move(110,100)

        self.autornameSelecterLabel = Label("autor name |",self)
        self.autornameSelecterLabel.move(285,50)
        self.autornameSelecter = Input(self)
        self.autornameSelecter.move(285,100)
        

        self.informationInputlabel = Label("about book",self)
        self.informationInputlabel.move(465,50)
        self.informationInput = InfoInput(self)
        self.informationInput.move(465,100)

        #Insert qilish uchun button qo'shamiz
        self.insertBtn = Btn("Insert",self)
        self.insertBtn.move(500,400)
        self.insertBtn.clicked.connect(self.__insert)
    
    
    def __insert(self):
        name = self.nameSelecter.text()
        autor_name = self.autornameSelecter.text()
        info = self.informationInput.toPlainText()
        database.insert(name, autor_name, info)
        self.nameSelecter.setText("")
        self.autornameSelecter.setText("")
        self.informationInput.setPlainText("")




app = QApplication([])

oyna = Window()
oyna.show()

app.exec()

