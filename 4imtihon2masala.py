def soncount(matn : str):
    sonlar = []
    soncha = ""
    for i in range(len(matn)):
        if (matn[i].isalpha()) and len(soncha) > 0:
            sonlar.append(int(soncha))
            soncha = ""
        if matn[i].isdigit():
            soncha += matn[i]
    if len(soncha) > 0:
        sonlar.append(int(soncha))
    return len(set(sonlar))
print(soncount( "leet1234code234"))