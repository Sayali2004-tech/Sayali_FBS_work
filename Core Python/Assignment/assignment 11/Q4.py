def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
numbers = [12, 45, 23, 67, 34, 89]
sorted_numbers = bubble_sort(numbers)
print("Second Largest Number:", sorted_numbers[-2])