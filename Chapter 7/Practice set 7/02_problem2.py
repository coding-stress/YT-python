#write a program to greet all the person names stored in a list 'l' and which starts with S.

l = ["Harry","Soham","Sachin","Suraj"]

for name in l :
    # print()
    if(name.startswith("S")):
        print(f"hello {name}")