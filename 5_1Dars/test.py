from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel

app=QApplication([])
oyna=QWidget()
oyna.setGeometry(300,400,400,600)

button1=QPushButton("1",oyna)
button1.setGeometry(180,280,50,50)
button1.setStyleSheet("""border-radius: 25px;
                      border: 1px solid black""")

buttonplus=QPushButton("+",oyna)
buttonplus.setGeometry(180,380,50,50)

buttonteng=QPushButton("=",oyna)
buttonteng.setGeometry(180,460,50,50)
def bir():
    txt=lineedit.text()+'1'
    lineedit.setText(txt)
def plus():
    txt = lineedit.text()
    if txt[-1] == "+":
        return
    if txt[-1] in ["-", "*", "/"]:
        txt = txt[:-1]
    lineedit.setText(txt + "+")

def teng():
    txt=lineedit.text()
    lineedit.setText(str(eval(txt)))

lineedit=QLineEdit(oyna)
lineedit.setGeometry(100,200,200,50)
lineedit.setStyleSheet("""border: 1px solid black;
                       font-size: 40px""")

button1.clicked.connect(bir)
buttonplus.clicked.connect(plus)
buttonteng.clicked.connect(teng)



oyna.show()
app.exec()
