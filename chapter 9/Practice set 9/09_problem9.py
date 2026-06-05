# write a program to find out whether a file is identical & matches the content of another file.

with open("this.txt") as f:
    content = f.read()

with open("this_copy.txt") as f:
    content1 = f.read()

if (content == content1):
    print("YES this file are identical")

else:
    print("NO this file are identical")
