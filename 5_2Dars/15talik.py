from os import system
system("cls")
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import random
koordinatalar = [[10,10,100,100],[120,10,100,100],[230,10,100,100],[340,10,100,100],[10,120,100,100],[120,120,100,100],[230,120,100,100],[340,120,100,100],[10,230,100,100],[120,230,100,100],[230,230,100,100],[340,230,100,100],[10,340,100,100],[120,340,100,100],[230,340,100,100],[340,340,100,100]]
tanlanganlar = []
winlist = [[10,10,100,100,1],[120,10,100,100,2],[230,10,100,100,3],[340,10,100,100,4],[10,120,100,100,5],[120,120,100,100,6],[230,120,100,100,7],[340,120,100,100,8],[10,230,100,100,9],[120,230,100,100,10],[230,230,100,100,11],[340,230,100,100,12],[10,340,100,100,13],[120,340,100,100,14],[230,340,100,100,15]]
buttons = []
buttonsinfo = []
class window(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        global koordinatalar, tanlanganlar, buttons, buttonsinfo, winlist
        self.setWindowTitle("15talik")
        self.setFixedSize(450,450)
        
        self.button1 = QPushButton(self)
        self.button2 = QPushButton(self)
        self.button3 = QPushButton(self)
        self.button4 = QPushButton(self)
        self.button5 = QPushButton(self)
        self.button6 = QPushButton(self)
        self.button7 = QPushButton(self)
        self.button8 = QPushButton(self)
        self.button9 = QPushButton(self)
        self.button10 = QPushButton(self)
        self.button11 = QPushButton(self)
        self.button12 = QPushButton(self)
        self.button13 = QPushButton(self)
        self.button14 = QPushButton(self)
        self.button15 = QPushButton(self)
        buttons.append(self.button1)
        buttons.append(self.button2)
        buttons.append(self.button3)
        buttons.append(self.button4)
        buttons.append(self.button5)
        buttons.append(self.button6)
        buttons.append(self.button7)
        buttons.append(self.button8)
        buttons.append(self.button9)
        buttons.append(self.button10)
        buttons.append(self.button11)
        buttons.append(self.button12)
        buttons.append(self.button13)
        buttons.append(self.button14)
        buttons.append(self.button15)
        print(koordinatalar)
        print("koordinatalar1")
        for i in range(len(buttons)):
            
            kordinata = random.choice(koordinatalar)
            while kordinata[:4] in tanlanganlar:

                kordinata = random.choice(koordinatalar)
            tanlanganlar.append(kordinata[:4])
            
            buttons[i].setText(str(i+1))
            buttons[i].setGeometry(kordinata[0],kordinata[1],kordinata[2],kordinata[3])
            kordinata.append(i+1)
            buttonsinfo.append(kordinata)
            for i in range(len(koordinatalar)):
                koordinatalar[i] = koordinatalar[i][:4]
        print(tanlanganlar)
        print("tanlanganlar")
        
        print(koordinatalar)
        print("koordinatalar2")
        print(buttonsinfo)
        print("--------buttonsinfo---------")
        self.button1.clicked.connect(lambda: self.buttonclick(self.button1))
        self.button2.clicked.connect(lambda: self.buttonclick(self.button2))
        self.button3.clicked.connect(lambda: self.buttonclick(self.button3))
        self.button4.clicked.connect(lambda: self.buttonclick(self.button4))
        self.button5.clicked.connect(lambda: self.buttonclick(self.button5))
        self.button6.clicked.connect(lambda: self.buttonclick(self.button6))
        self.button7.clicked.connect(lambda: self.buttonclick(self.button7))
        self.button8.clicked.connect(lambda: self.buttonclick(self.button8))
        self.button9.clicked.connect(lambda: self.buttonclick(self.button9))
        self.button10.clicked.connect(lambda: self.buttonclick(self.button10))
        self.button11.clicked.connect(lambda: self.buttonclick(self.button11))
        self.button12.clicked.connect(lambda: self.buttonclick(self.button12))
        self.button13.clicked.connect(lambda: self.buttonclick(self.button13))
        self.button14.clicked.connect(lambda: self.buttonclick(self.button14))
        self.button15.clicked.connect(lambda: self.buttonclick(self.button15))


        self.show()
    
    def buttonclick(self, button: QPushButton):
        global koordinatalar, tanlanganlar, buttons, buttonsinfo, winlist
        print(koordinatalar)
        print("koordinatalar")
        breakmi = False
        for kordinata in koordinatalar:
            if breakmi:
                break
            if kordinata not in tanlanganlar:
                button.setGeometry(kordinata[0],kordinata[1],kordinata[2],kordinata[3])
                for buttoninfo in buttonsinfo:
                    if buttoninfo[4] == int(button.text()):
                        tanlanganlar.remove(buttoninfo[:4])
                        tanlanganlar.append(kordinata[:4])
                        print(tanlanganlar)
                        print("------tanlanganlar-----------")
                        print(buttoninfo[:4])
                        print("-------buttoninfo[:4]----------")
                        buttonsinfo.remove(buttoninfo)
                        kordinata.append(int(button.text()))
                        buttonsinfo.append(kordinata[:5])
                        breakmi = True
                        break
        for i in range(len(koordinatalar)):
            koordinatalar[i] = koordinatalar[i][:4]
        breakmi = False
        print(koordinatalar)
        print("koordinatalarlast")
        print(tanlanganlar)
        print("------tanlanganlarlst-----------")
        print(buttonsinfo)
        print("buttunsinfolast")

                
            


app = QApplication([])
oyna = window()
app.exec()  