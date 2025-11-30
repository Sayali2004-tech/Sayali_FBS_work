def remove_even(lst):
    new_lst = []
    for i in lst:
        if i % 2 != 0:
            new_lst.append(i)
    return new_lst

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]

print("List after removing even numbers:", remove_even(lst))
