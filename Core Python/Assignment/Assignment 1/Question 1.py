
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)


total_marks = sum(marks)
percentage = (total_marks / 500) * 100  

print("\n----- Result -----")
print(f"Total Marks = {total_marks}/500")
print(f"Percentage = {percentage:.2f}%")
