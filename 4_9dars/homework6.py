from os import system
system("cls")
class Car:
    def __init__(self, brands : list) -> None:
        self.brands  = brands 
    def brand_exists(self, carcha : str) -> bool:
        if carcha in self.brands:
            return True
        return False
carlar = Car(["BMW", "Mers", "Chevrolet", "BYD", "TOYOTO"])
print(carlar.brand_exists("Salomat"))