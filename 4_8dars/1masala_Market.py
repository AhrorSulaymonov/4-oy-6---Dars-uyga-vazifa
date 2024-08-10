from os import system
system("cls")
def bigger_price(son : int, lst : list) -> list:
    lst = sorted(lst, key = lambda x : x["price"], reverse = True)
    lst2 = []
    for i in range(son):
        lst2.append(lst[i])
    return lst2
son = 2
lst = [
    {"name":"bread", "price" : 100},
    {"name":"wine", "price" : 138},
    {"name":"meat", "price" : 15},
    {"name":"water", "price" : 1}
]
print(bigger_price(son, lst))