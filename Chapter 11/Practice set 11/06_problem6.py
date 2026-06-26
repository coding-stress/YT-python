class twoDvector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k "
    

#creating Object
v = threeDvector(7, 8, 10)

print(v)