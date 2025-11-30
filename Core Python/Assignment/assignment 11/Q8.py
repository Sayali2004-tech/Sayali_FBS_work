n = 10
for i in range(n):
    row = []
    start = i * n + 1
    end = start + n
    row = list(range(start, end))
    if i % 2 != 0: 
        row.reverse()
    print(row)