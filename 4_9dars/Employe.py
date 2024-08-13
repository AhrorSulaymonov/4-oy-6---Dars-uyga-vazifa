class Employee:
    def __init__(self, id : int, firstName : str, lastName : str, salary : int) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
    def getId(self):
        return self.id
    def getfirstName(self):
        return self.firstName
    def getlastName(self):
        return self.lastName
    def getsalary(self):
        return self.salary
    def getAnnualSalary(self):
        return 12 * self.salary
    def raiseSalary(self, newsalary : int):
        self.salary = newsalary
    def toString(self):
        javob = f"Employee [id={self.id}, name={self.firstName} {self.lastName}, salary={self.salary}]"
        return javob

jahon = Employee(404,"Jahongir","Baxti tashkinskiy", 77000000)
print(jahon.getId())
print(jahon.toString())