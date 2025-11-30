radius = 20
length = 50
breadth = 40
cost_per_meter = 35
circle_half = 3.14159 * radius  
rectangle = 2 * (length + breadth)
total_length = circle_half + rectangle
total_wire = total_length * 5
total_cost = total_wire * cost_per_meter
print(f"Total cost of fencing: ₹{total_cost:.2f}")