from os import system
system("cls")
class  University:
    def __init__(self) -> None:
        self.name = "Milliy"
    def info(self):
        return f"University nomi = {self.name}"
class Staff(University):
    def __init__(self, first_name, last_name, age) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def more_info(self):
        return super().info() + f"""
first_name = {self.first_name}
last_name = {self.last_name}
age = {self.age}"""
class Student(Staff):
    def __init__(self, first_name, last_name, age, group) -> None:
        super().__init__(first_name, last_name, age)
        self.group = group
    def more_info(self):
        return super().more_info() + f"""
group = {self.group}
"""
class Teacher(Staff):
    def __init__(self, first_name, last_name, age, position, subject) -> None:
        super().__init__(first_name, last_name, age)
        self.position = position
        self.subject = subject
    def more_info(self):
        return super().more_info() + f"""
position = {self.position}
subject = {self.subject}
"""
class OtherStaff(Staff):
    def __init__(self, first_name, last_name, age, position) -> None:
        super().__init__(first_name, last_name, age) 
        self.position = position
    def more_info(self):
        return super().more_info() + f"""
position = {self.position}
"""
other = OtherStaff("Ahror", "Sulaymonov", 19, "Qoravul")
print(other.more_info())