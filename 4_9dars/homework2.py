from os import system
system("cls")
class Bino:
    def __init__(self, balandligi : float, rangi : str) -> None:
        self.balandligi = balandligi
        self.rangi = rangi
lst = [1,2,3,4,5]
lst[0] = Bino(45.6, "qizil")
lst[1] = Bino(45.6, "qizil")
lst[2] = Bino(55.6, "yashil")
lst[3] = Bino(65.6, "qizil")
lst[4] = Bino(24.5, "oq")
for i in lst:
    if i.balandligi > 50:
        print(i.rangi)