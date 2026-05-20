#write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 35% in each subject to pass. Assume 3 subjects and take marks as an input from user.

sub1 = int(input("Enter marks: "))
sub2 = int(input("Enter marks: "))
sub3 = int(input("Enter marks: "))

total =(sub1+sub2+sub3)

total_percentage = (total/300*100)

# total_percentage = print(total/300*100)

if(total_percentage>40):
    print("pass")

else:
    print("fail")