# Diamond Pattern (🔥 Important)
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *  for n = 4

n = int(input("enter the number : "))

for i in range (1,n+1):
        print(" "*(n-i),end="")
        print("*"*(2*i-1),end="")
        print("")
        print(" "*(n-2),end="")
        print("*"*(2*i-1),end="")
        print("")
        
