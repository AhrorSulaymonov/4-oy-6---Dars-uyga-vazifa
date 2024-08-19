from os import system
import numpy as np
system("cls")

def orol(a : list, i0 : int , j0 : int):
    length = len(a)
    length2 = len(a[0])
    for i in range(length):
        for j in range(length2):
            if a[i][j] == 1 and abs(i0 - i) <=1 and abs(j0 - j) <= 1:
                a[i0][j0] = 0
                i0 = i
                j0 = j
                orol(a,i0,j0)
a = [[1,1],[0,0],[1,1],[0,0],[1,0]]
length = len(a)
length2 = len(a[0])
for i in range(length):
    for j in range(length2):
        print(a[i][j],end=" ")
    print("\n")

countorol = 0

for i in range(length):
    for j in range(length2):
        if a[i][j] == 1:
            countorol += 1
            orol(a,i,j)
print(countorol)
