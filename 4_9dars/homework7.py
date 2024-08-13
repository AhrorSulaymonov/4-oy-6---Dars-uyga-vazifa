from os import system
system("cls")
class Hechqanday:
    def __init__(self) -> None:
        pass
    def get_string(self):
        self.string = input()
    def update_string(self) -> None:
        self.string = self.string[0].upper() + self.string[1:-1] + self.string[-1].upper()
a = Hechqanday()
a.get_string()
a.update_string()
print(a.string)