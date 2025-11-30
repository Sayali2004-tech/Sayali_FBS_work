def remove_element(lst, x):
    new_lst = []
    for i in lst:
        if i != x:
            new_lst.append(i)
    return new_lst

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]
x = int(input("Enter element to remove: "))

print("List after removal:", remove_element(lst, x))
