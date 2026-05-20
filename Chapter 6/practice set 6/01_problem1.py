#write a program to find the greatest of four numbers entered by the user.

a = int(input("Enter the number :"))
b = int(input("Enter the number :"))
c = int(input("Enter the number :"))
d = int(input("Enter the number :"))

# if(a>b,c,d):
#     print("a is greater")
# elif(b>a,c,d):
#     print("b is greater")
# elif(c>a,b,d):
#     print("c is greater")
# else:
#     print("d is greater")

if(a>b and a>c and a>d):
    print("greatest number is a.")

elif(b>a and b>c and b>d):
    print("greatest number is b.")

elif(c>a and c>b and c>d):
    print("greatest number is c.")

else:
    print("greatest number is d.")