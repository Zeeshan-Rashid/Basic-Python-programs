num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

greatest = num1

if num2 > greatest:
    greatest = num2
if num3 > greatest:
    greatest = num3

print("\nThe greatest number is:", greatest)
