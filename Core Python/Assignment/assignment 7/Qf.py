n = 5
for i in range(1, n+1):
    if i == 1:
        for j in range(1, n+1):
            print(j, end=" ")
        print()
    else:
        print(" " * 4 * (i - 1), end="")
        print(i)