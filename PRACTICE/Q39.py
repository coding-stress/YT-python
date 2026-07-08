# Swap two variables without using a third variable.

# Example:

# Before:
# a = 5
# b = 10

# After:
# a = 10
# b = 5

a = 5 
b = 10

a = a+b
b = a-b
a = a-b
print(a , b)