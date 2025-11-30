def separate_even_odd(lst):
    even = []
    odd = []
    for i in lst:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]

even_lst, odd_lst = separate_even_odd(lst)
print("Even elements:", even_lst)
print("Odd elements:", odd_lst)
