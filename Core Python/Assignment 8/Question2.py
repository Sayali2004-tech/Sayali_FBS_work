#Write a program to calculate area of circle
def area_of_circle(radius):
    pi = 3.14159
    return pi * radius * radius

# main program
r = float(input("Enter radius of circle: "))

area = area_of_circle(r)
print("Area of circle =", area)
