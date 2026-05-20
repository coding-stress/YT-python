# Write a python program using function to convert Celsius to fahrenheit.

 

def c_to_f(f):
    c = 5*(f-32)/9

f = int(input("enter temperature : "))
c = 5*(f-32)/9
print(f"{round(c,2)} degree Celsius")