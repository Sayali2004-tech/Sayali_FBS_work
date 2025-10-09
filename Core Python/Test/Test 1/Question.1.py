import math
l = float(input("Enter length of rectangle: "))
b = float(input("Enter breadth of rectangle: "))
r = float(input("Enter radius of semicircle: "))
area = (l * b) + (0.5 * math.pi * r * r)
perimeter = (2 * l) + (math.pi * r) + (2 * r)

print("Area of figure =", round(area, 2))
print("Perimeter of figure =", round(perimeter, 2))