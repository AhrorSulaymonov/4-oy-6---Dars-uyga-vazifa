from os import system
system("cls")
class Lstliclass:
    def __init__(self, numbers) -> None:
        self.numbers = numbers
    def delete_first_item(self):
        self.numbers = self.numbers[1:]
lst = Lstliclass(["birinchi",2,3,4,5,6,7,8])
lst.delete_first_item()
print(lst.numbers)