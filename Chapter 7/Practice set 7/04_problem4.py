# write a program to find weather a given number is prime or not.
n = int(input("enter the number : "))

for i in range(2 , n ):
    if(n%i) == 0:
        print(f"{n} This is not a Prime number.")
        break

else:
    print(f"{n} This is a prime number.")
