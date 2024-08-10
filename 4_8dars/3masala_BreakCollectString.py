from os import system
from json import dumps
system("cls")
file = open ("input.txt", "r")
gap = file.read()
L = []
for i in range(len(gap)):
    L.append(gap[:i+1])
for i in range(1, len(gap)):
    L.append(gap[:len(gap)-i])
print(dumps(L, indent=4))