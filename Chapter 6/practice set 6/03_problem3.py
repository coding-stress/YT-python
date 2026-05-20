# A spam comment is defined as a text containing following keywords: "Make a lot of money", "buy now","Subscribe this","click this". write a program to detect these spam.

# spam_keywords = ("Make a lot of money", "buy now","Subscribe this","click this")

p1="Make a lot of money"
p2="buy now"
p2="Subscribe this"
p3="click this"

message = input("Write a message \n")

if((p1 in message) or (p2 in message) or (p3 in message)):
    print("This is a spam")
else:
    print("this is not a spam")