# Write a recurcive function to calculate the sum of the first n natural munbers:

# n = int(input(" Enter a natural number : "))

# def natural_number(n):
#     a = n*(n+1)/2

# print(natural_number)

'''
sun(1) = 1 
sun(2) = 1+2
sun(3) = 1+2+3
sun(4) = 1+2+3+4
sun(5) = 1+2+3+4+5

sun (n) = 1+2+3+4.......n
sun(n) = sum(n-1)

'''
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

n = int(input(" Enter a natural Number : "))
print(sum(n))
