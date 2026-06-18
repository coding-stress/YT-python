class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("constructor of Programmer")
    b = 2

class manager(Programmer):
    def __init__(self):
        super().__init__()
        print("constructor of Manager ")
    c = 3

# o = Employee()
# print(o.a) #print the a attribute
# # print(o.b) # Shows an error as there is no b attribute in Employee class 

# o = Programmer()
# print(o.a,o.b)

o = manager()
print(o.a, o.b, o.c)