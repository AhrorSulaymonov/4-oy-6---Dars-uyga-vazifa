from os import system
system("cls")

def atoi(string : str):
    soncha = ""
    string = string.strip()
    for i in string:
        if i.isalpha():
            break
        if i == "-" and "-" not in soncha:
            soncha += "-"
        if soncha == "-" and i =="0":
            continue
        if i.isdigit():
            soncha += i
    if len(soncha) > 0 and soncha != "-":
        soncha = int(soncha)
        return soncha
    return 0




string = input("input: ")

print(atoi(string))