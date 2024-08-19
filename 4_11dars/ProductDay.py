from os import system
from datetime import date
system("cls")
class Product:
    def __init__(self, name : str, price : float, make_date : str) -> None:
        self.name = name
        self.price = price
        make_date = make_date.split("-")
        self.make_date = date(int(make_date[0]), int(make_date[1]), int(make_date[2]))
    def __str__(self) -> str:
        return f"""
    Nomi : {self.name}
    Narxi : {self.price}$
    Ishlab chiqarilgan yili : {self.make_date}"""
class Farm(Product):
    def __init__(self, name: str, price: float, make_date: str, date_price : str) -> None:
        super().__init__(name, price, make_date)
        date_price = date_price.split("-")
        self.date_price = date(int(date_price[0]), int(date_price[1]), int(date_price[2]))
    def __str__(self) -> str:
        farq = self.date_price - self.make_date
        return super().__str__() + f"""
    Magazinga kelgan sana : {self.date_price}
    Ishlab chiqarilganidan magazinga kelgunicha {farq.days} kun o'tgan
"""
Moshina = Farm("moshina", 20000, "2022-04-05","2023-03-05")
print(Moshina)