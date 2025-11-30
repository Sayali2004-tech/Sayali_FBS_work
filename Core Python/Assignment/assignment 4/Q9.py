start = int(input("Enter the starting number of range: "))
end = int(input("Enter the ending number of range: "))
divisor = int(input("Enter the divisor: "))
print(f"Numbers between {start} and {end} divisible by {divisor}:")
for i in range(start, end+1):
    if i % divisor == 0:
        print(i, end=" ")