from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from components import Label,ComboBox 
from os import system
system("cls")

class Window(QWidget):
    PLACES = [
    "Men",
    "Ikki eshik orasi",
    "UFQ",
    "O'tkan kunlar",
    "Mehrobdan chayon",
    "Ikkara ikki besh",
    "Choliqushi",
    "Yulduzli tunlar",
    "Imomning maniken qizi",
    "Mirzo Ulug'bek"  
]
    BOOK_INFO = {
        "Men": "Bu asar nafs haqidagi asardir.",
        "Ikki eshik orasi":"Asarda insonlar taqdiri va inson umrining murakkabligini mahorat bilan tasvirlangan." ,
        "UFQ":"Roman O'zbekiston mustaqilligi yillarida boshqa nashriyotlar tomonidan ham ko'p bora qayta nashr etildi",
        "O'tkan kunlar":"O'tgan kunlar o'zbek yozuvchisi Abdulla Qodiriy qalamiga mansub o'zbek adabiyotidagi ilk roman.",
        "Mehrobdan chayon":"Xudoyorxon va munshiylari hayotidan tarixiy ro'mon",
        "Ikkara ikki besh":" Asar to'liq yumor tarzida yozilgan, ko'zingiz yoshlangunga qadar kuldiradigan sahnalarga boy.",
        "Choliqushi":"Asarda yosh o'qituvchi Farida va uning Komronga bo'lgan muhabbati va har qanday qiyinchilikka dosh beraoladigan qiz,o'qituvchi haqida so'z yuritiladi.",
        "Yulduzli tunlar":"Asarda Zahiriddin Muhammad Bobur hayoti haqida so'z yuritiladi.",
        "Imomning maniken qizi":"Mazkur asar imomning qizi Fotimaning o'z oilaviy sharoitlaridan nolishi va ko'ngli to'lmasligi bilan boshlanadi.",
        "Mirzo Ulug'bek":"Mirzo Ulug'bek haqida. Mirzo Ulug'bek hayoti. Mirzo Ulug'bek biografiyasi. Ulug'bekning ilmiy merosi. Ulug'bek rasadxonasi. Ziji ko'ragoniy asari."                               
        }
  
    def __init__(self):
        super().__init__()

        self.resize(1200, 700)
        self.move(400, 200)

        self.placesLabel = Label("Kitoblarni ko'rish", self)
        self.placesLabel.move(50, 80)

        self.placesComboBox = ComboBox(self)
        self.placesComboBox.move(50, 120)


        self.placesComboBox.addItem("Tanlang...")
        self.placesComboBox.addItems(self.PLACES)

        
        self.placesComboBox.currentIndexChanged.connect(self.show_book_info)

    def show_book_info(self):
        book_name = self.placesComboBox.currentText()
        print(book_name)
        
        if book_name in self.BOOK_INFO:
            print("kitob topildi")
            info = self.BOOK_INFO[book_name]
            QMessageBox.information(self, book_name, info)
        elif book_name == "Tanlang...":
            pass  
        else:
            QMessageBox.warning(self, "Xato", "Bu kitob haqida ma'lumot yo'q.")

          
app = QApplication([])
oyna = Window()
oyna.show()
app.exec()
