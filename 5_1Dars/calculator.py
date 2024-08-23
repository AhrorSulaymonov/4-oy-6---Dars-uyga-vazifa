from os import system
system("cls")
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon, QColor, QPalette

calculator = QApplication([])
oyna = QWidget()
oyna.setWindowIcon(QIcon("calculatoricon.png"))
oyna.setWindowTitle("Calculator")
oyna.setGeometry(500, 200, 399, 628)
oyna.setStyleSheet("""
background-color: rgb(30, 30, 30);
color: rgb(255, 255, 255);
QPushButton {{
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
    }}
""")

bir = QPushButton(oyna)
bir.setText("1")
bir.setGeometry(1, oyna.height() - int(oyna.height()/10)*2 - 1,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
bir.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
ikki = QPushButton(oyna)
ikki.setText("2")
ikki.setGeometry(1*2 + int(oyna.width()/4), oyna.height() - int(oyna.height()/10)*2 - 1,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
ikki.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
uch = QPushButton(oyna)
uch.setText("3")
uch.setGeometry(1*3 + int(oyna.width()/4) * 2, oyna.height() - int(oyna.height()/10)*2 - 1,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
uch.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
qoshuv = QPushButton(oyna)
qoshuv.setText("+")
qoshuv.setGeometry(1*4 + int(oyna.width()/4) * 3, oyna.height() - int(oyna.height()/10)*2 - 1,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
qoshuv.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
tort = QPushButton(oyna)
tort.setText("4")
tort.setGeometry(1, oyna.height() - int(oyna.height()/10)*3 - 1*2,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
tort.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
besh = QPushButton(oyna)
besh.setText("5")
besh.setGeometry(1*2 + int(oyna.width()/4), oyna.height() - int(oyna.height()/10)*3 - 1*2,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
besh.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
olti = QPushButton(oyna)
olti.setText("6")
olti.setGeometry(1*3 + int(oyna.width()/4)*2, oyna.height() - int(oyna.height()/10)*3 - 1*2,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
olti.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
ayiruv = QPushButton(oyna)
ayiruv.setText("-")
ayiruv.setGeometry(1*4 + int(oyna.width()/4)*3, oyna.height() - int(oyna.height()/10)*3 - 1*2,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
ayiruv.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
yetti = QPushButton(oyna)
yetti.setText("7")
yetti.setGeometry(1, oyna.height() - int(oyna.height()/10)*4 - 1*3,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
yetti.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
sakkiz = QPushButton(oyna)
sakkiz.setText("8")
sakkiz.setGeometry(1 * 2 + int(oyna.width()/4), oyna.height() - int(oyna.height()/10)*4 - 1*3,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
sakkiz.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
toqqiz = QPushButton(oyna)
toqqiz.setText("9")
toqqiz.setGeometry(1 * 3 + int(oyna.width()/4) * 2, oyna.height() - int(oyna.height()/10)*4 - 1*3,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
toqqiz.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
kopaytiruv = QPushButton(oyna)
kopaytiruv.setText("x")
kopaytiruv.setGeometry(1 * 4 + int(oyna.width()/4) * 3, oyna.height() - int(oyna.height()/10)*4 - 1*3,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
kopaytiruv.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
qaramaqarshi = QPushButton(oyna)
qaramaqarshi.setText("+/-")
qaramaqarshi.setGeometry(1, oyna.height() - int(oyna.height()/10),int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
qaramaqarshi.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
nol = QPushButton(oyna)
nol.setText("0")
nol.setGeometry(1*2 + int(oyna.width()/4), oyna.height() - int(oyna.height()/10),int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
nol.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
nuqta = QPushButton(oyna)
nuqta.setText(".")
nuqta.setGeometry(1*3 + int(oyna.width()/4) * 2, oyna.height() - int(oyna.height()/10),int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
nuqta.setStyleSheet("""
    background-color: #7F7878;
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
tenglik = QPushButton(oyna)
tenglik.setText("=")
tenglik.setGeometry(1*4 + int(oyna.width()/4) * 3, oyna.height() - int(oyna.height()/10),int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
tenglik.setStyleSheet("""
    background-color: rgb(139, 166, 252);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
teskari = QPushButton(oyna)
teskari.setText("1/x")
teskari.setGeometry(1, oyna.height() - int(oyna.height()/10)*5 - 1*4,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
teskari.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
kvadrat = QPushButton(oyna)
kvadrat.setText("x²")
kvadrat.setGeometry(1*2 + int(oyna.width()/4), oyna.height() - int(oyna.height()/10)*5 - 1*4,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
kvadrat.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
kvadrat_ildiz = QPushButton(oyna)
kvadrat_ildiz.setText("²√x")
kvadrat_ildiz.setGeometry(1*3 + int(oyna.width()/4) * 2, oyna.height() - int(oyna.height()/10)*5 - 1*4,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
kvadrat_ildiz.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
bolish = QPushButton(oyna)
bolish.setText("÷")
bolish.setGeometry(1*4 + int(oyna.width()/4) * 3, oyna.height() - int(oyna.height()/10)*5 - 1*4,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
bolish.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
foiz = QPushButton(oyna)
foiz.setText("%")
foiz.setGeometry(1, oyna.height() - int(oyna.height()/10)*6 - 1*5,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
foiz.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
CE = QPushButton(oyna)
CE.setText("CE")
CE.setGeometry(1*2 + int(oyna.width()/4), oyna.height() - int(oyna.height()/10)*6 - 1*5,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
CE.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
C = QPushButton(oyna)
C.setText("C")
C.setGeometry(1*3 + int(oyna.width()/4) * 2, oyna.height() - int(oyna.height()/10)*6 - 1*5,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
C.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
back = QPushButton(oyna)
back.setText("<-")
back.setGeometry(1*4 + int(oyna.width()/4) * 3, oyna.height() - int(oyna.height()/10)*6 - 1*5,int(oyna.width()/4)-1, int(oyna.height()/10) - 1)
back.setStyleSheet("""
    background-color: rgb(50, 50, 50);
    color: white;
    border-radius: 10px;
    border: 1px solid rgb(80, 80, 80);
""")
textbox_Main = QLineEdit(oyna)
textbox_Main.setPlaceholderText("0")
textbox_Main.setStyleSheet("""
border : 2px solid white;
font-size : 40px ;
border-radius: 10px;
""")
textbox_Main.setGeometry(1, oyna.height() -  int(int(oyna.height()/10)*6.7) - 1*5  - int(int(oyna.height()/10)*1.7), oyna.width() - 2, int(int(oyna.height()/10)*1.7))
def birdef():
    txt=textbox_Main.text()+'1'
    if txt == "01":
        txt = "1"
    textbox_Main.setText(txt)

def ikkidef():
    txt=textbox_Main.text()+'2'
    if txt == "02":
        txt = "2"
    textbox_Main.setText(txt)

def uchdef():
    txt=textbox_Main.text()+'3'
    if txt == "03":
        txt = "3"
    textbox_Main.setText(txt)

def tortdef():
    txt=textbox_Main.text()+'4'
    if txt == "04":
        txt = "4"
    textbox_Main.setText(txt)

def beshdef():
    txt=textbox_Main.text()+'5'
    if txt == "05":
        txt = "5"
    textbox_Main.setText(txt)

def oltidef():
    txt=textbox_Main.text()+'6'
    if txt == "06":
        txt = "6"
    textbox_Main.setText(txt)

def yettidef():
    txt=textbox_Main.text()+'7'
    if txt == "07":
        txt = "7"
    textbox_Main.setText(txt)

def sakkizdef():
    txt=textbox_Main.text()+'8'
    if txt == "08":
        txt = "8"
    textbox_Main.setText(txt)

def toqqizdef():
    txt=textbox_Main.text()+'9'
    if txt == "09":
        txt = "9"
    textbox_Main.setText(txt)

def noldef():
    txt=textbox_Main.text()+'0'
    if txt == "00":
        txt = "0"
    textbox_Main.setText(txt) 
def plus():
    txt = textbox_Main.text()
    if txt[-1] == "+":
        return
    if txt[-1] in ["-", "*", "/"]:
        txt = txt[:-1]
    textbox_Main.setText(txt + "+")
def minus():
    txt = textbox_Main.text()
    if txt[-1] == "-":
        return
    if txt[-1] in ["+", "*", "/"]:
        txt = txt[:-1]
    textbox_Main.setText(txt + "-")
def kopaytir():
    txt = textbox_Main.text()
    if txt[-1] == "*":
        return
    if txt[-1] in ["-", "+", "/"]:
        txt = txt[:-1]
    textbox_Main.setText(txt + "*")
def bol():
    txt = textbox_Main.text()
    if txt[-1] == "/":
        return
    if txt[-1] in ["-", "*", "+"]:
        txt = txt[:-1]
    textbox_Main.setText(txt + "/")
def teng():
    txt=textbox_Main.text()
    try:
        # Amallarni hisoblaymiz
        textbox_Main.setText(str(eval(txt)))
    except ZeroDivisionError:
        # Agar nolga bo'lish amali bo'lsa
        textbox_Main.setText("Nolga bo'lish mumkin emas")
        textbox_Main.setStyleSheet("""
        font-size : 18px
""")
    except Exception as e:
        textbox_Main.setText(f"Xatolik: {e}")
        textbox_Main.setStyleSheet("""
        font-size : 18px
""")
    
def Cdef():
    textbox_Main.setText("")
    textbox_Main.setPlaceholderText("0")
def teskaridef():
    txt=textbox_Main.text()
    if txt != '0' and len(txt) != 0:
        textbox_Main.setText(str(1/(float(txt)))[:14])
def kvadratdef():
    txt=textbox_Main.text()
    if (float(txt))**2 % 1 == 0:
        textbox_Main.setText(str((int(txt))**2))
        return
    textbox_Main.setText(str((float(txt))**2))
    
def nuqtadef():
    txt = textbox_Main.text() + "."
    textbox_Main.setText(txt)
def kvadrat_ildizdef():
    txt = textbox_Main.text()
    if (float(txt)**(1/2)) % 1 == 0:
        textbox_Main.setText(str(int(float(txt)**(1/2))))
        return
    textbox_Main.setText(str(float(txt)**(1/2)))
def backdef():
    txt = textbox_Main.text()[:-1]
    textbox_Main.setText(txt)
def qaramaqarshidef():
    txt = textbox_Main.text()
    if txt[0] == "-":
        txt = "+" + txt[1:]
    elif txt[0].isdigit():
        txt = "-" + txt
    elif txt[0] == "+":
        txt = "-" + txt[1:]
    textbox_Main.setText(txt)
bir.clicked.connect(birdef)
ikki.clicked.connect(ikkidef)
uch.clicked.connect(uchdef)
tort.clicked.connect(tortdef)
besh.clicked.connect(beshdef)
olti.clicked.connect(oltidef)
yetti.clicked.connect(yettidef)
sakkiz.clicked.connect(sakkizdef)
toqqiz.clicked.connect(toqqizdef)
nol.clicked.connect(noldef)
teskari.clicked.connect(teskaridef)

qoshuv.clicked.connect(plus)
ayiruv.clicked.connect(minus)
kopaytiruv.clicked.connect(kopaytir)
bolish.clicked.connect(bol)
tenglik.clicked.connect(teng)
kvadrat.clicked.connect(kvadratdef)
C.clicked.connect(Cdef)
nuqta.clicked.connect(nuqtadef)
kvadrat_ildiz.clicked.connect(kvadrat_ildizdef)
back.clicked.connect(backdef)
qaramaqarshi.clicked.connect(qaramaqarshidef)
CE.clicked.connect(Cdef)

oyna.show()
calculator.exec()
