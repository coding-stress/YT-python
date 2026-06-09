# Create a class "Programmer"for storing information of few programmers working at Microsoft.

class programmers:
    company = "Microseft"
    
    def __init__(self,name,salary,code):
        self.name = name 
        self.salary = salary
        self.code = code

s = programmers("Suraj",1500000, 1234)
print(s.name, s.salary, s.code)

a = programmers("Abhishek","*****", 1111)
print(a.name, a.salary, a.code)