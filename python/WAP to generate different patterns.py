# // Right angled triangle pattern

# Pyramid pattern

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print("")

#  Right angled triangle pattern
n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print("")

#Inverted Right angled triangle pattern

n = int(input("Enter the number of rows: "))

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

#. Diamond pattern

n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print("")

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print("")

#