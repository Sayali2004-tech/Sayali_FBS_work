num_students = int(input("Enter number of students: "))

percentages = []

for i in range(num_students):
    print(f"\nEnter marks of 5 subjects for student {i+1}:")
    
    total = 0
    for j in range(5):
        mark = float(input(f"  Subject {j+1}: "))
        total += mark
    
    percentage = (total / 500) * 100
    percentages.append(percentage)

# Display percentages
print("\n--- Student Percentages ---")
for i, p in enumerate(percentages, start=1):
    print(f"Student {i}: {p:.2f}%")

# Calculate average percentage
average = sum(percentages) / num_students
print(f"\nAverage Percentage: {average:.2f}%")
