class Employee:
    language = "Python" #this is a class attribute
    salary = 1200000

    def __init__(self,name,salary,language): #dunder method which is autometically called
        self.name = name
        self.salary = salary
        self.language =language

        print("I'm creating an object")

    def getInfo(self):
        print(f"the language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("hello everyone")

codingstress = Employee("Abhishek",1500000,"JAVA")

codingstress.name = "CodingStress"
print(codingstress.name, codingstress.salary, codingstress.language)

# abhishek = Employee()