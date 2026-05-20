'''
1 for snake 
- 1 for water
0 for gun
'''

import random

computer = random.choice([-1,0,1])
youstr = input("Enter your choice : ")
youdict = {"s" : 1, "w": -1, "g" : 0}
reversedict = {1: "snake", -1: "water", 0 : "gun"}

you = youdict[youstr]

# by now we have 2 numbers (variables), you and computer 

print (f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if (computer == you ):
    print("its a draw ")

else:
    if(computer == -1 and you == 1):
        print("You win")
        print("computer Lose")
    
    elif(computer == -1 and you == 0 ):
        print("You Lose")
        print("computer wins")

    elif(computer == 1 and you == -1):
        print("You Lose")
        print("computer win")

    elif(computer == 1 and you == 0):
        print("You win")
        print("computer Lose")
        

    elif(computer == 0 and you == 1 ):
        print("You win")
        print("computer Lose")
    
    elif( computer == 0 and you == -1 ):
        print("You win")
        print("computer Lose")
    
    else:
        print("somthing is wrong !")