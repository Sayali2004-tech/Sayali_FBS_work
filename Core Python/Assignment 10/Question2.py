#Write a program to find maximum and minimum element in a list.
# Function to find maximum element
def find_max(lst):
    max_val = lst[0]
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

# Function to find minimum element
def find_min(lst):
    min_val = lst[0]
    for i in lst:
        if i < min_val:
            min_val = i
    return min_val

# Main program
n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    lst.append(num)

print("Maximum element =", find_max(lst))
print("Minimum element =", find_min(lst))
