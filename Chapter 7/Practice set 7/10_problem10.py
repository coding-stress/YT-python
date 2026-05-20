# write a program to print multiplication table of n using for loop in reverse order

t = int(input("Enter the number of table you want : "))
for i in reversed(range(1 , 11)):
    print(f"{t} X {i} = {t*i}")