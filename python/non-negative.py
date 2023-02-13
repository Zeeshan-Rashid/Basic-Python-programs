def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

x = int(input("Enter a non-negative integer: "))

result = factorial(x)

print("The factorial of", x, "is:", result)
