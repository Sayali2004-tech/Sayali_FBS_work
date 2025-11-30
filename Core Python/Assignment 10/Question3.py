def second_largest(lst):
    max_val = lst[0]
    second = lst[0]
    for i in lst:
        if i > max_val:
            second = max_val
            max_val = i
        elif i > second and i != max_val:
            second = i
    return second

n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input(f"Element {i+1}: ")))

print("Second largest element =", second_largest(lst))
