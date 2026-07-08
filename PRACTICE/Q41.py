# Take a three-digit number and print the sum of its digits.

# Example:

# Input:
# 456

# Output:
# 15/

num1 = int(input("Enter Three digit number : "))

result = sum(int(digit) for digit in str(num1)) # I solve this line using ai.

print(result)