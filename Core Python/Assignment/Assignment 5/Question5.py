amount = int(input("Enter amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

count = 0
remaining = amount

print("Notes used:")

for note in notes:
    if remaining >= note:
        num_notes = remaining // note
        remaining %= note
