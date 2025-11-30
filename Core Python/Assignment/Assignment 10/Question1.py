#Write a program to find sum of all elements of list
# Function to calculate sum of elements
def sum_of_list(lst):
    total = 0
    for i in lst:
        total += i
    return total

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)

print("Sum of all elements =", sum_of_list(lst))
