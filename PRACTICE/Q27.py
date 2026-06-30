# Three-Number Averager

# Modify the average program from your files to accept three separate numbers from the user and calculate their exact mathematical average. Remember to use proper parentheses to ensure correct order of operations!

# Concept: Operator precedence, floating-point division (/).

a = int(input("Inter a Number for a : "))
b = int(input("Inter a Number for b : "))
c = int(input("Inter a Number for c : "))

print(f"The average of {a}, {b} and {c} is ", (a+b+c)/3 )