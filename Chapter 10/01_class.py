class Employee:
    language = "py" # this is a class attribute
    salary = "1500000"

suraj = Employee()
suraj.name = "Suraj" # this is an instance attribute
print(suraj.name, suraj.salary, suraj.language)



abhishek = Employee()
abhishek.name = "Abhishek Singh"  
print(abhishek.name, abhishek.salary, abhishek.language)

# Here name is instance attribute and salary and language are class attribute as they directly belong to the class.