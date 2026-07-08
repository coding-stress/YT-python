# Check whether a person can donate blood.

# Conditions:

# Age ≥18
# Weight ≥50 kg
 
age = int(input("Enter your age : "))
weight = int(input("Enter Ypur weight : "))

if(age >= 18) and (weight >= 50):
    print("You can donate blood.")
else:
    print("You can not donate blood.")