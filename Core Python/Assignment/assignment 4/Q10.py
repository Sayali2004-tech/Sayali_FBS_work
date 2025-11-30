n = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_divisors += i
if sum_of_divisors == n and n != 0:
    print(f"{n} is a Perfect Number")
else:
    print(f"{n} is not a Perfect Number")