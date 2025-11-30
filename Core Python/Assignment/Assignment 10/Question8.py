def duplicate_list(lst):
    new_lst = []
    for i in lst:
        new_lst.append(i)
    return new_lst

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]

dup_lst = duplicate_list(lst)
print("Original list:", lst)
print("Duplicated list:", dup_lst)
