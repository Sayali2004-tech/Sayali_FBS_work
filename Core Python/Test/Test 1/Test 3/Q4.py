#Write a program to print pattern 10101 01010 10101 01010 10101

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        # Sum of row index and column index determines 1 or 0
        if (i + j) % 2 == 0:
            print("1", end="")
        else:
            print("0", end="")
    print()  # Move to next line
