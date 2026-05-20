# write a program to greet all the person names stored in a list 'l' and which starts with S.

l = ["Abhishek","neha","Suraj","Sonam"]

for name in l:
    if(name.startswith("S")):
        print(f"hello {name}")