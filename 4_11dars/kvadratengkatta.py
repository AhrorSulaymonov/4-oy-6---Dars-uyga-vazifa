from os import system
system("cls")

kvlar = []
sinf = 0

def fillsinfmatrix(a : list):
    global sinfmatrix
    length = len(a)
    length2 = len(a[0])
    for i in range(length):
        matrixcha = []
        for j in range(length2):
            matrixcha.append(0)
        sinfmatrix.append(matrixcha)


def kvadrat(a : list, i0 : int, j0 : int):
    length = len(a)
    length2 = len(a[0])
    ilar = [1]
    jlar = [1]
    kvtomoni = 1
    for i in range(i0, length):
        for j in range(j0, length2):
            

            # if a[i][j] == 1 and (abs(i0 - i) ==1 and abs(j0 - j) == 0 or abs(i0 - i) == 0 and abs(j0 - j) == 1):
            #     ivaj = max[i,j,i0,j0]
            #     if a[ivaj][ivaj] != 1:
            #         a[i0][j0] = 0
            #     else:
            #         kvtomoni += 1
            #         ilar.append(i)
            #         jlar.append(j)
            #         ilar[0] = 2
                    