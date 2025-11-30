num_passengers = int(input("Enter number of passengers: "))
ticket_cost = float(input("Enter cost per ticket: "))

total_amount = 0

for i in range(num_passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))

    if age < 12:
        amount = ticket_cost * 0.70   # 30% discount
    elif age > 59:
        amount = ticket_cost * 0.50   # 50% discount
    else:
        amount = ticket_cost          # full price

    total_amount += amount

print(f"\nTotal ticket amount for all passengers: ₹{total_amount:.2f}")
