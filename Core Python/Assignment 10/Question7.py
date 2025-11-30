def cube_list(lst):
    cubed = []
    for i in lst:
        cubed.append(i**3)
    return cubed

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]

print("Cubed list:", cube_list(lst))
