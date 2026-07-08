# Check whether a character is a vowel or consonant.

vowel = "a e i o u"

character = input("Enter a character : ")

character = character.lower() #used to convert input into lower case.

if character.isalpha() and len(character) == 1:
    if(character in vowel):
        print("Yes a vowel in this character")
    else:
        print("No vowel in this character")
else:
    print("Invalid input. Please enter a single letter of the alphabet.")