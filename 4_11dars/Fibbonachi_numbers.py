from os import system
import math
system("cls")


fibbonachies = [1,1]
N = int(input("Piramidani nechinchi fibbonachi sonigacha tuzay:\n--> "))
if N > 2:
    for i in range(N-2):
        fibbonachies.append(fibbonachies[i] + fibbonachies[i+1])
print(fibbonachies)
# 
satrcount = math.ceil((-1+((8*N + 1)**(1/2)))/2)
print(satrcount)
distanc = satrcount - 1
print(distanc)
index = 0
pleace = len(str(fibbonachies[-1]))
for i in range(satrcount):
    print(" " * pleace * (distanc - i),end="")
    for j in range(i+1):
        if j == i  and index < len(fibbonachies):
            print(("%" + str(pleace) + "d")% (fibbonachies[index]))
            index += 1
        elif index < len(fibbonachies):
            print(("%" + str(pleace) + "d")% (fibbonachies[index]), end = " ")
            index += 1