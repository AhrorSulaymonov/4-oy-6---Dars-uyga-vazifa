from os import system
system("cls")
class Class:
    def __init__(self, my_list: list) -> None:
        self.my_list = my_list
    def delete_last_item(self):
        self.my_list = self.my_list[:-1]
lstcha = Class([1,2,4,5,"salom"])
lstcha.delete_last_item()
print(lstcha.my_list)
