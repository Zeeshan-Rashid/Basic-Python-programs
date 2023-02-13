def find_minimum(a, b):
    if a < b:
        return a
    else:
        return b

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

result = find_minimum(x, y)

print("The minimum of", x, "and", y, "is:", result)
