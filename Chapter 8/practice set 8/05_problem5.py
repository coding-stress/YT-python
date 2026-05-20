# write a python function to print first n lines of the folloeing pattern:
# ***
# **
# * 
#  for n = 3

'''
def star(n):
    for i in range (1 , n+1):
        print("*"*(n-i+1), end="")
        print(" "*(n-i), end="")
        print("")


n = int(input("enter a number : "))
print(star(n))
'''
def pattern(n):
    if (n==0):
        return
    print("*"*n)
    pattern(n-1)

pattern(3)