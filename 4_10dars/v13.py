from os import system
system("cls")
class Shape:
    def __init__(self) -> None:
        pass
class Line(Shape):
    def __init__(self) -> None:
        pass
    def shakl_chiz(self, uzn : int):
        print("*" * uzn)
class Uchburchak(Shape):
    def __init__(self) -> None:
        pass
    def shakl_chiz(self, uzn : int):
        for i in range(uzn):
            for j in range(uzn):
                if j == 0 or i == uzn - 1 or j == i:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("\n") 
class Kvadrat(Shape):
    def __init__(self) -> None:
        pass
    def shakl_chiz(self, uzn : int):
        for i in range(uzn):
            for j in range(uzn):
                if j == 0 or i == uzn - 1 or i == 0 or j == uzn - 1:
                    print("*",end="")
                else:
                    print(" ",end="")
            print("\n")
ln = Line()
uchbur = Uchburchak()
kv = Kvadrat()
ln.shakl_chiz(8)
uchbur.shakl_chiz(7)
kv.shakl_chiz(6)