#Repeat program 4 for a list of such words to be censored.



words = ["donkey","bad"]

#used for read the txt file.

with open ("mumbai.txt") as f :
    content = f.read()

for word in words:
    content = content.replace(word, "#"* len(word))

with open("mumbai.txt","w") as f:
    f.write(content)