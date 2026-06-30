# Write a program to print third, fifth and seventh element from a list using enumerate function.

Games = ["BGMI", "Roblox", "Chess", "Mystery House", "Puzzle", "Dr.Drive", "Gun game", "Golf", "Combat"]

for index, item in enumerate(Games):
    if index in [2,4,6]:
        print(f"The element at this position is {index+1} amd game is {item}")