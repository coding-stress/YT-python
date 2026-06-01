# Write a program to generate multiplaction table from 2 to 20 and write it to the different files. place this files in a folder for a 13 - year old.


def generatetable(n):
    table = "" #this variable is used to store all values in it 
    for i in range (1 , 11):
        table += f"{n} X {i} = {n*i}\n"

    with open(f"Tables/table_{n}.txt", "w") as f: # use .txt to make it writable formate using Table/table_{n} for generate new file to store new table
        f.write(table)


for i in range (2 , 21):
    generatetable(i)

print("table is printed.")