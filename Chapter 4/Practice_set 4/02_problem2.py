#write a program to accept marks of 6 Students and display them in a sorted manner.
45
marks = []

marks.append(int(input("enter marks : ")))
marks.append(int(input("enter marks : ")))
marks.append(int(input("enter marks : ")))
marks.append(int(input("enter marks : ")))
marks.append(int(input("enter marks : ")))
marks.append(int(input("enter marks : ")))
# print(marks)

marks.sort()
print(marks)