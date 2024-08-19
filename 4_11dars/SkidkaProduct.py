from os import system
from datetime import date
system("cls")
class Product:
    def __init__(self, name : str, price : float, manufacturer : str) -> None:
        self.name = name
        self.price = price
        self.manufacturer = manufacturer
    def __str__(self) -> str:
        return f"""
    Nomi : {self.name}
    Narxi : {self.price}$
    Ishlab chiqaruvchi : {self.manufacturer}"""


class Market(Product):
    skidka_ishladi = False
    def __init__(self, name: str, price: float, manufacturer: str, date_creat : str, product_sale : float) -> None:
        super().__init__(name, price, manufacturer)
        self.date_creat = date_creat
        self.product_sale = product_sale
    def go_skidka(self):
        a = str(date.today()).split("-")
        b = self.date_creat.split("-")
        if int(a[0]) - int(b[0]) > 2 or int(a[0]) - int(b[0]) == 2 and int(a[1]) - int(b[1]) > 1 or int(a[0]) - int(b[0]) == 2 and int(a[1]) - int(b[1]) == 1 and int(a[2]) - int(b[2]) > 0:
            self.price *= (1-(self.product_sale / 100))
            skidka_ishladi = True
    def __str__(self) -> str:
        return super().__str__() + f"""
    Ishlab chiqatilgan sanasi : {self.date_creat}
"""
olma = Market("Olma", 2.5, "Apple garden", "2021-01-02", 14.5)
print(olma)
olma.go_skidka()
print(olma)