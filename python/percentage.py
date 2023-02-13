maths = float(input("Enter marks in Mathematics: "))
english = float(input("Enter marks in English: "))
science = float(input("Enter marks in Science: "))
history = float(input("Enter marks in History: "))
geography = float(input("Enter marks in Geography: "))

total_marks = maths + english + science + history + geography
percentage = (total_marks / 500) * 100

print("\nThe total marks are:", total_marks)
print("The percentage is:", percentage, "%")
