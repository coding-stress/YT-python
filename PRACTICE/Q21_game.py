import random

def game():
    print("you are playing a game...")
    score = random.randint(1 , 50) #to generate random number from 1 to 50 

    with open("practice_highscore.txt") as f:
        highscore = f.read()
        if (highscore != ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"score is {score}")
    if (score > highscore):

        with open("practice_highscore.txt", "w") as f:
            f.write(str(score))
            print(f"high score is {score}")

    return score

game ()