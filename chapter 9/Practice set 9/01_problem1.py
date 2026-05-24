# Write a program to read the text from a given file 'poem.txt' and find out whether it contains the word 'teinkle'.

f = open("poem.txt")

poem = f.read()
if("twinkle" in poem):
    print("the word twinkle is present in the poem ")

else:
    print(" The word Twinklw is not present in the poem ")
f.close()