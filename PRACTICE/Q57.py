# Calculate grade based on marks:

# 90–100 → A
# 75–89 → B
# 60–74 → C
# Below 60 → Fail

marks = int(input("Enter marks : "))

if(marks <= 100 ) and (marks >= 90):
    print("A")
elif(marks <= 89 ) and (marks >= 75):
    print("B")
elif(marks <= 74 ) and (marks >= 60):
    print("C")
elif(marks <= 60):
    print("Fail")