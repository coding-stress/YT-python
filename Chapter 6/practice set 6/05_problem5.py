# write a program which finds out whether a given name is present in a list or not.

name = ["Abhishek","Neha","Suraj","Ashish","Tanya"]

a = input("Enter name : ")

if(a in name):
    print(a)
    print("Yes, this name is in the list")
else:
    print(a)
    print("No, this name is not in the list")