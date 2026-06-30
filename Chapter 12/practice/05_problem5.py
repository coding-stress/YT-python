num = int(input("Enter a number : "))

Table = [ f"{num} X {i} = {num*i}" for i in range (1 , 11) ]

# print(*Table,sep="\n")

with open("Table.txt", "w") as f:
    # f.write(str(Table))
    print(*Table,sep="\n",file=f) # This line helps to print new line after one loop is completed.