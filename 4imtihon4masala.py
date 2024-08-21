from os import system
system("cls")
class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary
    def get_details(self) -> str:
        return f"""
Ismi : {self.name}
Oyligi : {self.salary}"""
    def calculate_bonus(self) -> float:
        return 0.0
class Manager(Employee):
    def __init__(self, name: str, salary: float,  department: str) -> None:
        super().__init__(name, salary)
        self.department = department
    def get_details(self) -> str:
        return super().get_details() + f"""
Kafedrasi : {self.department}
"""
    def calculate_bonus(self) -> float: # - Bonusni hisoblaydi (10% bonus).
        return self.salary * 0.1
class Developer(Employee):
    def __init__(self, name: str, salary: float, programming_language: str) -> None:
        super().__init__(name, salary)
        self.programming_language = programming_language
    def get_details(self) -> str:
        return super().get_details() + f"""
Dasturlash tili : {self.programming_language}
"""
    def calculate_bonus(self) -> float: # - Bonusni hisoblaydi (5% bonus).
        return self.salary * 0.05

# Klassdan foydalanish

manager = Manager(name="Alice", salary=120000, department="Sales")
# Yangi Manager yaratildi, ism: Alice, maosh: 120000, bo'lim: Sales

developer = Developer(name="Bob", salary=100000, programming_language="Python")
# Yangi Developer yaratildi, ism: Bob, maosh: 100000, dasturlash tili: Python

print(manager.get_details())
# Manager: Alice, Department: Sales, Salary: 120000

print(developer.get_details())
# Developer: Bob, Programming Language: Python, Salary: 100000

print(manager.calculate_bonus())
# Manager uchun bonus: 12000 so'm (10%)

print(developer.calculate_bonus())
# Developer uchun bonus: 5000 so'm (5%)