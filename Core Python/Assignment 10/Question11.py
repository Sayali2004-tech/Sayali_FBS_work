def divisible_by(lst, m, n):
    res = []
    for i in lst:
        if i % m == 0 and i % n == 0:
            res.append(i)
    return res

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]
m = int(input("Enter m: "))
n_div = int(input("Enter n: "))

print("Numbers divisible by both:", divisible_by(lst, m, n_div))
