def numbers_squares_cubes(lst):
    squares = []
    cubes = []
    for i in lst:
        squares.append(i**2)
        cubes.append(i**3)
    return lst, squares, cubes

n = int(input("Enter number of elements: "))
lst = [int(input(f"Element {i+1}: ")) for i in range(n)]

numbers, squares, cubes = numbers_squares_cubes(lst)
print("Numbers:", numbers)
print("Squares:", squares)
print("Cubes:", cubes)
