def calculation(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    return add, subtract, multiply

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

result = calculation(x, y)

print("The addition of", x, "and", y, "is:", result[0])
print("The subtraction of", x, "and", y, "is:", result[1])
print("The multiplication of", x, "and", y, "is:", result[2])
