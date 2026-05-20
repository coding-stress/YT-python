# Write a program using functions to find greatest of three numbers.

a = int(input("Enter your Number :"))
b = int(input("Enter your Number :"))
c = int(input("Enter your Number :"))

def greatest():
    if(a > b and a > c):
        return a
    elif(b > a and b > c):
        return b
    elif( c > a and c > b):
        return c

print(greatest())