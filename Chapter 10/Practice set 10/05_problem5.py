# Write a class Train which has methods to book a ticket, get status (no of seates ) and get fare information of train running under Indian Railway.

from random import randint

class train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self,fro,to):
        print(f"ticket is booked in train no: {self.trainNo} from {fro} to {to}")
    
    def getstatus(self):
        print(f"train no: {self.trainNo} is running on the time")

    def getfare(self,fro ,to):
        print(f"ticket fare in tain no : {self.trainNo} from {fro} to {to} is {randint(111,9999)}")

t= train(12999)
t.book("Anand Vihar ", "jharkhand")
t.getstatus()
t.getfare("Anand Vihar ", "jharkhand")