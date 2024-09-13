from math import ceil
from os import system
system("cls")
def evalRPN(tokens: list[str]) -> int:
    operators = ["+", "-", "*", "/"]

    while len(tokens) > 1:
        for i in tokens:
            if i in operators:
                indx =  tokens.index(i)
                if i == "+":
                    son = int(tokens[indx-2]) + int(tokens[indx-1])
                    tokens = tokens[:indx-2] + [str(son)] + tokens[indx+1:]
                    print(tokens)
                elif i == "-":
                    son = int(tokens[indx-2]) - int(tokens[indx-1])
                    tokens = tokens[:indx-2] + [str(son)] + tokens[indx+1:]
                    print(tokens)
                elif i == "/":
                    if abs(int(tokens[indx-2])) < abs(int(tokens[indx-1])):
                        son = 0
                    else:
                        son = ceil(int(tokens[indx-2]) / int(tokens[indx-1]))
                    tokens = tokens[:indx-2] + [str(son)] + tokens[indx+1:]
                    print(tokens)
                elif i == "*":
                    son = int(tokens[indx-2]) * int(tokens[indx-1])
                    tokens = tokens[:indx-2] + [str(son)] + tokens[indx+1:]
                    print(tokens)
    return tokens[0]
print(evalRPN(["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]))


