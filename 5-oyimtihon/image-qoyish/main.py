from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QListWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from os import system, getcwd

system("cls")

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(900, 700)

        users = [
            {"imageUrl": "abrormuxtoraliy.jpg", "text": "Abrormuxtoraliy"},
            {"imageUrl": "afandi.png", "text": "Afandi"},
            {"imageUrl": "AfruzaH.png", "text": "AfruzaH"},
            {"imageUrl": "alishersadullaev.jpg", "text": "Alishersadullaev"},
            {"imageUrl": "anziratxola.jpg", "text": "Anziratxola"},
            {"imageUrl": "baxtiyorjumaev.jpg", "text": "Baxtiyorjumaev"},
            {"imageUrl": "bekzodmirahmedov.png", "text": "Bekzodmirahmedov"},
            {"imageUrl": "bobursattarov.png", "text": "Bobursattarov"},
            {"imageUrl": "isomjon.jpg", "text": "Isomjon"},
            {"imageUrl": "jahongirvakhidov.jpg", "text": "Jahongirvakhidov"},
            {"imageUrl": "javokhirsindarov.png", "text": "Javokhirsindarov"},
            {"imageUrl": "marjona.png", "text": "Marjona"},
            {"imageUrl": "muhammadaliabdurakhmonov.jpg", "text": "Muhammadaliabdurakhmonov"},
            {"imageUrl": "NilufarY.png", "text": "NilufarY"},
            {"imageUrl": "NodiraN.png", "text": "NodiraN"},
            {"imageUrl": "nodirbekabdusattorov.png", "text": "Nodirbekabdusattorov"},
            {"imageUrl": "nodirbekyakkuboev.png", "text": "Nodirbekyakkuboev"},
            {"imageUrl": "qunduzamaki.jpg", "text": "Qunduzamaki"},
            {"imageUrl": "safarmurod.png", "text": "Safarmurod"},
            {"imageUrl": "shamsiddinvokhidov.png", "text": "Shamsiddinvokhidov"},
            {"imageUrl": "shumbola.png", "text": "Shumbola"},
            {"imageUrl": "teacherazam.jpg", "text": "Teacherazam"},
            {"imageUrl": "ulugbekismatov.png", "text": "Ulugbekismatov"},
            {"imageUrl": "ulugbektillayev.jpg", "text": "Ulugbektillayev"},
            {"imageUrl": "UmidaOmonova.png", "text": "UmidaOmonova"},
            {"imageUrl": "xushnudbek.jpg", "text": "Xushnudbek"}
        ]

        
        self.listWidget = QListWidget(self)
        self.listWidget.resize(800, 600)
        self.listWidget.move(50, 50)
        self.listWidget.setStyleSheet("color: white; font-weight: bold; background-image: url(./images/image.png); background-position: center;")


        for user in users:
            self.addItem(f"./images/{user["imageUrl"]}", user["text"])



    def addItem(self, url: str, text: str):
        icon = QIcon(url)
        item = QListWidgetItem(icon, text)

        size = QSize()
        size.setHeight(100)
        size.setWidth(400)

        self.listWidget.setIconSize(size)
        self.listWidget.addItem(item)


app = QApplication([])

oyna = Window()
oyna.show()

app.exec()