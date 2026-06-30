# Write a program to display a/b where a and b are integers. If b = 0, display infinite by handling the 'ZeroDivisionError'.

a= 5
b= 0

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbes by zero")
else:
    print(f"The division a/b is {a/b}")

