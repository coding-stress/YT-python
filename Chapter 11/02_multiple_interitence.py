class Employee:
    company = "ITC"
    name = "Default"
    def show(self):
        print ( F"The name of the Employee {self.name} and the Company is {self.company}")

class coder:
    language = "pyhton"
    def print_language(self):
        print(f"out of all the languages here is your language : {self.language}")


class Programmer(Employee , coder):
    company = "ITC Infoctech"
    def showLanguage(self):
        print(f"The name is {self.name } and he is good with {self.language}")

a = Employee()
b = Programmer()
c = coder()

b.show()
b.print_language()
b.showLanguage()


print(a.company , b.company , c.language )