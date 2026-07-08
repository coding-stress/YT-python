# Take a month number (1–12) and print the month's name.

# Method - 2

num = input("Enter a number of month : ")

if num.isdigit():
    num = int(num)

    if (1 <= num <= 12):
        if(num == 1):
            print("Jnaurary")
        elif(num == 2):
            print("February")
        elif(num == 3):
            print("March")
        elif(num == 4):
            print("April")
        elif(num == 5):
            print("May")
        elif(num == 6):
            print("June")
        elif(num == 7):
            print("July")
        elif(num == 8):
            print("August")
        elif(num == 9):
            print("September")
        elif(num == 10):
            print("October")
        elif(num == 11):
            print("November")
        elif(num == 12):
            print("December")
    else:
        print("Invalid input. Please enter a number from 1 to 12.")
else:
    print("Please enter only number")
