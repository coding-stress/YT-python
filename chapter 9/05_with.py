hi = "hey guys this is me "

f = open("file.txt","a")
print(f.write(hi))
f.close()

# the same can be written using with statement like this :

with open("file.txt") as f:
    print(f.read())

# you dont have to explicitly close the file