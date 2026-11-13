name = input("Enter your name: ")

subject1 = int(input("Enter marks for subject 1: "))
subject2 = int(input("Enter marks for subject 2: "))
subject3 = int(input("Enter marks for subject 3: "))

total = subject1 + subject2 + subject3
average = total / 3

if average >= 80 and average <= 100:
    grade = "A+"
elif average >= 70 and average <= 79:
    grade = "A"
elif average >= 60 and average <= 69:
    grade = "B"
elif average >= 50 and average <= 59:
    grade = "C"
else:
    grade = "F"
print()
print(f"Result of {name}")
print()
print(f"Student Name: {name}")
print(f"Total Marks: {total}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
