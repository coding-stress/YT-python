# Write a program to find wheather a given username contains less than 10 characters or not.

character_username = input("Enter user name : ")

if(len(character_username)>10):
    print("this is more than 10 characters in username")
else:
    print("this is less than 10 characters in username")