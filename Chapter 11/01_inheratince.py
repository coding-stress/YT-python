class Employee:
    company = "ITC"
    def show(self):
        print ( F"The name of the Employee {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infoctech"
    def showLanguage(self):
        print(f"The name is {self.name } and he is good with {self.language}")

a = Employee()
b= Programmer()

print(a.company , b.company )