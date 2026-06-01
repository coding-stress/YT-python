# A file cotain a word "Donkey" multiple times. you need to write a program which replace this word with ######by by updating the same file.
"""
f = open("mumbai.txt")
data = f.read()
print (data)

"""

with open("mumbai.txt") as f:
    data = f.read()
    
newdata = data.replace("donkey", "#####")

with open("mumbai.txt", "w") as f:
    f.write(newdata)