class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"the language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("hello everyone")

codingstress = Employee()
codingstress.language = "JAVA"

codingstress.getInfo()
codingstress.greet()
# Employee.getInfo(codingstress)