def check_element(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]
x = int(input("Enter number to check: "))

count = check_element(lst, x)
if count > 0:
    print(f"{x} is present {count} times")
else:
    print(f"{x} is not present in the list")
