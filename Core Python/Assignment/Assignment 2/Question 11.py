
amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]

note_count = {}

for note in notes:
    if amount >= note:
        note_count[note] = amount // note  
        amount = amount % note  

print("Minimum number of notes needed:")
for note, count in note_count.items():
    print(f"₹{note}: {count} note(s)")
