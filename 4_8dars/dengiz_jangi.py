from os import system
system("cls")
def dengizjangi(lst : license, koordinata : str) -> str:
    A_E = {
        "A" : 0,
        "B" : 1,
        "C" : 2,
        "D" : 3,
        "E" : 4
    }
    if lst[len(lst) -1 - A_E[koordinata[0]]][int(koordinata[1])-1] == "*":
        return "Booom"
    else:
        return "splash"
lst = [
    [".",".","*"],
    ["*",".","."],
    [".","*","."]
    ]
koordinata = "C1"
print(dengizjangi(lst,koordinata))