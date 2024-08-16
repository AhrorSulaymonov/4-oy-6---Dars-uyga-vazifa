from os import system
system("cls")
class Employee:
    def __init__(self, surname, position, salary) -> None:
        self.surname = surname
        self.position = position
        self.salary = salary
class Enterprise_employee(Employee):
    def __init__(self, surname, position, salary, rating) -> None:
        super().__init__(surname, position, salary)
        self.rating = rating
    def info(self):
        print(f"""
              
surname = {self.surname}
position = {self.position}
salary = {self.salary}
rating = {self.rating}
""")
enter1 = Enterprise_employee("Oybekov", "Backend", 14000000, 74)
enter2 = Enterprise_employee("Nuriddinov", "Frontend", 9000000, 68)
enter3 = Enterprise_employee("Nuriddinova", "UNIX", 9000000, 85)
enter4 = Enterprise_employee("Urinov", "UI", 8000000, 87)
enter5 = Enterprise_employee("G'anijonov", "Frontend", 9000000, 60)
lst = []
lst.append(enter1)
lst.append(enter2)
lst.append(enter3)
lst.append(enter4)
lst.append(enter5)
for i in lst:
    i.info()
for i in lst:
    if i.rating >= 60 and i.rating < 75:
        i.salary *= 1.2
    elif i.rating >= 75 and i.rating < 90:
        i.salary *= 1.4
    elif i.rating >= 90 and i.rating < 100:
        i.salary *= 1.6
for i in lst:
    i.info()