# The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ' Hi-score.txt' which is either blank or contains the previous high score whenever the game() function break the Hi-score.

import random

def game():
    print("you are playing a game..")
    score = random.randint(1 , 50 )
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore != ""):
           highscore = int(highscore)
        else:
            highscore = 0
    
    print(f"Your score is {score}")
    if(score>highscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))
            print(f"high score is : {score} ")
        return score
        

game()