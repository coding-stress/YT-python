# Age Difference Checker
# Ask two users to input their respective birth years (e.g., 2004 and 2006). Write code to calculate how many years apart they are. Hint: Subtract the smaller year from the larger one, or use subtraction.

# Concept: Integer subtraction and arithmetic logic.

a = int(input("Enter your birth year : "))
b = int(input("Enter your birth year : "))

if(a < b, b-a):
    print(f"The age difference is {a-b} ")

else:
    print(f"The age difference is {b-a} ")