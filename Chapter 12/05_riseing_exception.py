a= int(input("Enter a Number : "))
b= int(input("Enter a Number : "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide numbes by zero")
else:
    print(f"The division a/b is {a/b}")

