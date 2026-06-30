# String Concatenator vs. Math Sum
# Write a script that takes two inputs without casting them to integers. Print what happens when you use the + operator on them. Then, cast them to integers and print the + result again to show the difference between string concatenation and mathematical addition.

# Concept: String joining vs. integer addition.


a = input("Inter a Number for a : ")
b = input("Inter a Number for b : ")

print(f"The addition of a and b without changing it into integer is {a + b} ")

num1 = int(a)
num2 = int(b)

print(f"The addition of a and b after changing it into integer is {num1 + num2} ")