prices = []
for i in range(5):
    price = float(input(f"Enter price of product {i+1}: "))
    prices.append(price)
subtotal = sum(prices)
gst = subtotal * 0.18
total = subtotal + gst
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"GST (18%): ₹{gst:.2f}")
print(f"Total Bill: ₹{total:.2f}")