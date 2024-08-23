from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QCheckBox
from time import sleep
from os import system
system("cls")
class window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("BAA")
        self.resize(400, 600)
        self.BAAcheckbox = QCheckBox("BAA", self)
        self.BAAcheckbox.setStyleSheet("""
        font-size: 22px;
""")
        self.BAAcheckbox.adjustSize()
        self.BAAcheckbox.move(30, 100)

        self.Dubaicheckbox = QCheckBox("Dubai", self)
        self.Dubaicheckbox.setStyleSheet("""
        font-size: 22px;
""")
        self.Dubaicheckbox.adjustSize()
        self.Dubaicheckbox.move(50, 150)
        self.Dubaicheckbox.setEnabled(False)

        self.Al_Jahoncheckbox = QCheckBox("Al Jahon", self)
        self.Al_Jahoncheckbox.setStyleSheet("""
        font-size: 22px;
""")
        self.Al_Jahoncheckbox.adjustSize()
        self.Al_Jahoncheckbox.move(50, 200)
        self.Al_Jahoncheckbox.setEnabled(False)

        self.Al_Ahrorcheckbox = QCheckBox("Al Ahror", self)
        self.Al_Ahrorcheckbox.setStyleSheet("""
        font-size: 22px;
""")
        self.Al_Ahrorcheckbox.adjustSize()
        self.Al_Ahrorcheckbox.move(50, 250)
        self.Al_Ahrorcheckbox.setEnabled(False)


        self.BAAcheckbox.toggled.connect(lambda checked: self.BAAbosildi(self.BAAcheckbox,checked))


        self.RUSSIAcheckbox = QCheckBox("RUSSIA", self)
        self.RUSSIAcheckbox.setStyleSheet("""
        font-size: 22px;
""")
        self.RUSSIAcheckbox.adjustSize()
        self.RUSSIAcheckbox.move(30, 300)

        self.Moskvacheckbox = QCheckBox("Moskva", self)
        self.Moskvacheckbox.setStyleSheet("""
        font-size: 22px;
""")
        self.Moskvacheckbox.adjustSize()
        self.Moskvacheckbox.move(50, 350)
        self.Moskvacheckbox.setEnabled(False)


        self.Natashacheckbox = QCheckBox("Natasha", self)
        self.Natashacheckbox.setStyleSheet("""
        font-size: 22px;
""")
        self.Natashacheckbox.adjustSize()
        self.Natashacheckbox.move(50, 400)
        self.Natashacheckbox.setEnabled(False)


        self.Ozoncheckbox = QCheckBox("Ozon", self)
        self.Ozoncheckbox.setStyleSheet("""
        font-size: 22px;
""")
        self.Ozoncheckbox.adjustSize()
        self.Ozoncheckbox.move(50, 450)
        self.Ozoncheckbox.setEnabled(False)
        self.RUSSIAcheckbox.toggled.connect(lambda checked: self.RUSSIAbosildi(self.RUSSIAcheckbox,checked))

        
        self.show()

    def BAAbosildi(self, BAAcheckbox: QCheckBox, checked : bool):
        self.Dubaicheckbox.setEnabled(checked)
        self.Al_Jahoncheckbox.setEnabled(checked)
        self.Al_Ahrorcheckbox.setEnabled(checked)
        if not checked:
            self.Dubaicheckbox.setChecked(checked)
            self.Al_Jahoncheckbox.setChecked(checked)
            self.Al_Ahrorcheckbox.setChecked(checked)
    def RUSSIAbosildi(self, RUSSIAcheckbox: QCheckBox, checked : bool):
        self.Moskvacheckbox.setEnabled(checked)
        self.Natashacheckbox.setEnabled(checked)
        self.Ozoncheckbox.setEnabled(checked)
        if not checked:
            self.Moskvacheckbox.setChecked(checked)
            self.Natashacheckbox.setChecked(checked)
            self.Ozoncheckbox.setChecked(checked)
        


app = QApplication([])
oyna = window()
app.exec()