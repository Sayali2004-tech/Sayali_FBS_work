start = int(input("Enter the starting number of range: "))
end = int(input("Enter the ending number of range: "))
print(f"Armstrong numbers between {start} and {end} are:")
for num in range(start, end+1):    
    digits = str(num)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    if total == num:
        print(num, end=" ")