import mysql.connector
from colorama import init, Fore
from os import system

system("cls")

init(autoreset=True)


class database():
    def __init__(self) -> None:
        
        self.db = mysql.connector.connect(
        host     = "localhost",
        user     = "root",
        password = "2004"
        )
        self.kursor = self.db.cursor()

        self.kursor.execute("CREATE DATABASE IF NOT EXISTS KUTUBXONA;")
        print( Fore.GREEN+"* Databaza yaratildi!")

        self.kursor.execute("USE KUTUBXONA;")
        print(Fore.GREEN+"* Dtabazaga ulandi!")

        self.kursor.execute("""
            CREATE TABLE IF NOT EXISTS KITOBLAR(
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                author VARCHAR(255) NOT NULL,
                description TEXT NOT NULL
                    );
        """ )
        print(Fore.GREEN+"* Table yaratilindi!")

        self.kursor.execute("select count(*) from KITOBLAR")

        kitoblarsoni = self.kursor.fetchone()[0]
        print(kitoblarsoni)

        
        if kitoblarsoni == 0:
            self.kursor.execute("""INSERT INTO kitoblar VALUES (NULL, "MEN", "FOTIH DO'MAN", "Bu asar nafs haqidagi asardir."),
                            (NULL, "IKKI ESHIK ORASI", "O'TKIR HOSHIMOV", "Asarda insonlar taqdiri va inson umrining murakkabligini mahorat bilan tasvirlangan."),
                            (NULL, "UFQ", "Said Ahmad","Roman O'zbekiston mustaqilligi yillarida boshqa nashriyotlar tomonidan ham ko'p bora qayta nashr etildi"),
                            (NULL, "O'tkan kunlar", "Abdulla Qodiry", "O'tgan kunlar o'zbek yozuvchisi Abdulla Qodiriy qalamiga mansub o'zbek adabiyotidagi ilk roman."),
                            (NULL, "Mehrobdan chayon","Abdulla Qodiry","Xudoyorxon va munshiylari hayotidan tarixiy ro'mon"),
                            (NULL, "Ikkara ikki besh","O'tkir Hoshimov"," Asar to'liq yumor tarzida yozilgan, ko'zingiz yoshlangunga qadar kuldiradigan sahnalarga boy."),
                            (NULL, "Choliqushi","Rashid Nuri Guntekin","Asarda yosh o'qituvchi Farida va uning Komronga bo'lgan muhabbati va har qanday qiyinchilikka dosh beraoladigan qiz,o'qituvchi haqida so'z yuritiladi."),
                            (NULL, "Yulduzli tunlar"," Pirimqul Qodirov","Asarda Zahiriddin Muhammad Bobur hayoti haqida so'z yuritiladi."),
                            (NULL, "Imomning maniken qizi","Omina Shenliko'g'li","Mazkur asar imomning qizi Fotimaning o'z oilaviy sharoitlaridan nolishi va ko'ngli to'lmasligi bilan boshlanadi."),
                            (NULL, "Mirzo Ulug'bek","Maqsud SHayxzoda","Mirzo Ulug'bek haqida. Mirzo Ulug'bek hayoti. Mirzo Ulug'bek biografiyasi. Ulug'bekning ilmiy merosi. Ulug'bek rasadxonasi. Ziji ko'ragoniy asari.");""")
            
a = database()





