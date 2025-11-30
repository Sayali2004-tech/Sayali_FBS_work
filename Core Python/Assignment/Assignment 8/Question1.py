#(Use Functions in all programs)
#1. Write a program to calculate area of rectangle
def area_of_rectangle(length, width):
    return length * width

# main program
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))

area = area_of_rectangle(l, w)
print("Area of rectangle =", area)
