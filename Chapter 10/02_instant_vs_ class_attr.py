class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

suraj = Employee()
suraj.language = "JAVA" # THIS IS AN INSTANCE ATTRIBUTE
print(suraj.language, suraj.salary)