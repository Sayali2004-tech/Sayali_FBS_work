list_of_tuples = [(1, 3), (2, 2), (4, 1), (3, 5)]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
print("Sorted by second element:", sorted_list)