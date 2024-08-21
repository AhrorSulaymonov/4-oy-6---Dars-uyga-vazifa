def harxiltakrorlanish(lst : list):
    countlar = {}
    for i in lst:
        countlar[i] = lst.count(i)
    valuelar = list(countlar.values())
    for i in valuelar:
        if valuelar.count(i) > 1:
            return False
    return True
print(harxiltakrorlanish([-3,0, -3]))