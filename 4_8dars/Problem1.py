from os import system
system("cls")
son = input("Son kiriting: ")
dct = {}
for i in son:
    dct[i] = son.count(i)
dct = dict(sorted(dct.items()))
for key, value in dct.items():
    print(f"{key} - {value}")