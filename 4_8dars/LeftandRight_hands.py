from os import system
system("cls")
lefthand = ["q","w","e","r","t","a","s","d","f","g","z","x","c","v","b", "1", "!", "2","@","3","#","4","$","5","%"]
righthand = ["y","u","i","o","p","[",']','{','}','\\','|','h','j','k','l',';',':',"'",'"','n','m',',','<','.','>','/','?','6','7','8','9','0','-','=','^','&','*','(',')','_','+']
gap = input("gap kiriting: ")
chapcount = 0
ongcount = 0
for i in gap:
    if i in lefthand or (chr(ord(i)+32) in lefthand and chr(ord(i)+32).isalpha()) and i != " ":
        chapcount += 1
    elif i in righthand or (chr(ord(i)+32) in righthand and chr(ord(i)+32).isalpha()) and i != " ":
        ongcount += 1
print(f"O'ng qo'lda {ongcount} ta")
print(f"Chap qo'lda {chapcount} ta yozgan")