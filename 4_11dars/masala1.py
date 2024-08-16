from os import system
system("cls")
class Soldat:
    def __init__(self, firstname, lastname, age, high : float, weight : float, jins : str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.high = high
        self.weight = weight
        self.jins = jins
        if self.high < 150 or self.weight < 75:
            self.possesion = "Piyoda askar"
        else :
            self.possesion = "Tank qo'shinlari"
    def infobirinchishart(self):
        if self.age > 18 and (self.jins).lower() == "erkak":
            return f"""
firstname = {self.firstname}
lastname = {self.lastname}
age = {self.age}
high = {self.high}
weight = {self.weight}
jins = {self.jins}
"""
    def info(self):
        return f"""
firstname = {self.firstname}
lastname = {self.lastname}
age = {self.age}
high = {self.high}
weight = {self.weight}
jins = {self.jins}
pozetsiya = {self.possesion}
"""
        
Jaxon = Soldat('Jahon', 'rahimberdiyev', 18, 179, 86, "erkak")
print(Jaxon.info())
