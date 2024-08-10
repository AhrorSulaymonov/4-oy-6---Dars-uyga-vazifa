from os import system
system("cls")
son = input("Son kiriting: ")
dct = {}
for i in son:
    dct[i] = son.count(i)
print(dct)