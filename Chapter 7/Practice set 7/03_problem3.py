# solve problem 1 using while loop
n = int(input("enter your number : "))
i = 1
while( i in range (1,11)): # or we can use (i<11)
    
    print(f"{n} X {i} = {n*i}")
    i += 1