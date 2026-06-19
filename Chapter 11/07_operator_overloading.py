# class Number:
#     def __init__(self,n):
#         self.n = n

#     def __add__(self, num):
#         return self.n + num.n

# n = Number(1)
# m = Number(26)

# print(n + m)

class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):
        # Instead of returning an int, return a new Number object
        return Number(self.n + num.n)

n = Number(1)
m = Number(2)
o = Number(3)
p = Number(4)

# This will now work perfectly!
# print(n + m + o + p)
result = n + m + o + p
print(result.n)  # Output: 10