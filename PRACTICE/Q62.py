# Check whether a number is divisible by both 3 and 5.

num1 = int(input("Enter a number : "))

if (num1 % 3 == 0) and (num1 % 5 == 0 ):
    print(f"This Number {num1} is divisible by 3 and 5")

elif(num1 % 3 == 0) and (num1 % 5 != 0):
    print(f"this number {num1} is divisible by 3 and not divided by 5 ")

elif(num1 % 3 != 0) and (num1 % 5 ==0 ):
    print(f"this number {num1} is not divided by 3 and divided by 5")

elif(num1 % 3 != 0) and (num1 % 5 != 0):
    print(f"This Number {num1} is not divisible by both.")