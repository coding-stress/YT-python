import random
n = random.randint(1, 100)

a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("Guess the Number : "))
    if (a < n):
        print("Higher number plese")
    elif(a > n):
        print("Lower number please")

print(f"You Guessed the correct Number {n} in {guesses} attempts")