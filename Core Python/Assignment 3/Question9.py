marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)
total = sum(marks)
percentage = total / 5
print("Total Marks =", total)
print("Percentage =", percentage, "%")
if percentage >= 60:
    print("Grade: First Class")
elif percentage >= 50:
    print("Grade: Second Class")
elif percentage >= 40:
    print("Grade: Pass Class")
else:
    print("Grade: Fail")