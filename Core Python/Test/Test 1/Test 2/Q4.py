length = float(input("Enter length of wall: "))
height = float(input("Enter height of wall: "))
cost_per_sq_meter = float(input("Enter cost per square meter: "))
total_area = 4 * length * height
total_cost = total_area * cost_per_sq_meter
print(f"Total cost of painting: ₹{total_cost:.2f}")