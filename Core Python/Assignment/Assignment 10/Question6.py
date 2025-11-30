def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        duplicate = False
        for j in new_lst:
            if i == j:
                duplicate = True
                break
        if not duplicate:
            new_lst.append(i)
    return new_lst

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]

print("List without duplicates:", remove_duplicates(lst))
