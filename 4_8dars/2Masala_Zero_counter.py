from os import system
system("cls")
def Zero_counter(son : str) -> int:
    count = 0
    for i in son:
        if i =="0":
            count += 1
        else:
            return count
print(Zero_counter("1410"))