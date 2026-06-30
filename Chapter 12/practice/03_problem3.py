# Write a list comprehension to print a list which contains the multiplication table of a user entered number.

num = int(input("Enter a number : "))

Table = [ f"{num} X {i} = {num*i}" for i in range (1 , 11) ]

print(*Table,sep="\n")