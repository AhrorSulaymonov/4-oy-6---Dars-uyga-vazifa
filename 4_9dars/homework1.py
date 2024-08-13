from os import system
system("cls")
class Talaba:
    def __init__(self, ism : str, familiya : str, baho : float) -> None:
        self.ism = ism
        self.familiya = familiya
        self.baho = baho
T1 = Talaba("Aziz", "G'aybullayev", 70.4)
T2 = Talaba("Ilhom", "Abdurayimov", 80.5)
T3 = Talaba("Ahror", "Sulaymonov", 60.7)
if T1.baho < T2.baho and T1.baho < T3.baho:
    print(T1.ism)
elif T2.baho < T1.baho and T2.baho < T3.baho:
    print(T2.ism)
elif T3.baho < T2.baho and T3.baho < T1.baho:
    print(T3.ism)