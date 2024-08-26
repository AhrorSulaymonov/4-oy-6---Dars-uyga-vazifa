from os import system
system("cls")
kvlar = []


def kvadrataniqlash(matrit : list, i0, j0):
    kulonmatrit = []
    lingth1 = len(matritsa) - i0
    lingth2 = len(matritsa[0]) - j0
    uzunliklar = [lingth1, lingth2]
    minuzunlik = min(uzunliklar)
    breakmi = False
    for lingth in range(minuzunlik):
        if breakmi:
            break
        for i in range(lingth+1):
            if breakmi:
                break
            tomoncha = []
            for j in range(lingth+1):
                if matrit[i0 + i][j0 + j] == 1:
                    tomoncha.append(matrit[i0 + i][j0 + j])
                else:
                    tomoncha = []
                    breakmi = True
                    break
            if len(tomoncha) > 0:
                kulonmatrit.append(tomoncha)
        kvlar.append((len(kulonmatrit))**2)
        kulonmatrit = []
        
    
    
        


matritsa = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
lingth1 = len(matritsa)
lingth2 = len(matritsa[0])

for i in range(lingth1):
    for j in range(lingth2):
        if matritsa[i][j] == 1:
            i0 = i
            j0 = j
            kvadrataniqlash(matritsa,i0, j0)
print(max(kvlar))
    

