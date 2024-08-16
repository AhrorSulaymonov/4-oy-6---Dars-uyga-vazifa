from os import system
system("cls")
class Product:
    def __init__(self, name : str, price : float, make_date : str) -> None:
        year , month = make_date.split(":")
        self.name = name
        self.price = price
        self.make_date = make_date
    def __str__(self) -> str:
        return f"""
    Nomi : {self.name}
    Narxi : {self.price}$
    Ishlab chiqarilgan yili : {self.make_date}"""
class Farm(Product):
    def __init__(self, name: str, price: float, make_date: str, date : str) -> None:
        year , month = date.split(":")
        super().__init__(name, price, make_date)
        self.date = date
    def __str__(self) -> str:
        yearcome , monthcome = self.date.split(":")
        yearmake , monthmake = self.make_date.split(":")
        return super().__str__() + f"""
    Do'konga kelgan sana : {self.date}
    Ishlab chiqarilgandan dukonga kelguncha otgan oylar soni : {(int(yearcome) - int(yearmake)) * 12 + (int(monthcome) - int(monthmake))}
"""
Televezor = Farm("Artel 14 - avlod", 200.5, "2024:02","2025:03")
print(Televezor)