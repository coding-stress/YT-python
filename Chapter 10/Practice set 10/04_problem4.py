# Write a class "calculater" capable of finding square, cube and square root of a number.

class calcualter:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"the square is {self.n*self.n}")

    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n*self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello stressed !")

a = calcualter(4)
a.hello()
a.cube()
a.square()
a.squareroot()