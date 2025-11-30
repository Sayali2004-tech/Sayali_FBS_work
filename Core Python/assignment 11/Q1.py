numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_list = [x for x in numbers if x % 2 == 0]
odd_list = [x for x in numbers if x % 2 != 0]
print("Even List:", even_list)
print("Odd List:", odd_list)