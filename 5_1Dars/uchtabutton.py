from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtGui import QIcon

me = ["Ahror","Sulaymonov","Bahrom o'g'li"]


app = QApplication([])
oyna = QWidget()
oyna.setWindowTitle("Me")
oyna.setWindowIcon(QIcon("qamashi.jpg"))
oyna.setGeometry(200,400,500,500)
oyna.setStyleSheet("""
    background-color: #F4D03F;
    background-image: linear-gradient(132deg, #F4D03F 0%, #16A085 100%);
""")
about = QLabel(oyna)
about.setText("               ")
about.setStyleSheet("""
font-size = 25px
color = red
font-weight = 850
""")


ism = QPushButton(oyna)
ism.setText("ismim")
ism.setGeometry(30, 300, int(oyna.width()/3) - 50, 30)
def ism_bosildi():
    global me
    about.setText(me[0])
    about.move(int((oyna.width() - len(me[0]))/2), 100)
    about.adjustSize()
ism.clicked.connect(ism_bosildi)
familiya = QPushButton(oyna)
familiya.setText("familiya")
familiya.setGeometry(30 + ism.width() + 30, 300, int(oyna.width()/3) - 50, 30)
def familiya_bosildi():
    global me
    about.setText(me[1])
    about.move(int((oyna.width() - len(me[1]))/2), 100)
    about.adjustSize()
familiya.clicked.connect(familiya_bosildi)
sharifim = QPushButton(oyna)
sharifim.setText("sharifim")
sharifim.setGeometry(30 + ism.width() + 30 + familiya.width() + 30, 300, int(oyna.width()/3) - 50, 30)
def sharifim_bosildi():
    global me
    about.setText(me[2])
    about.move(int((oyna.width() - len(me[2]))/2), 100)
    about.adjustSize()
sharifim.clicked.connect(sharifim_bosildi)
oyna.show()
app.exec()
