n = int(input("Enter a number: "))
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact
sum_of_factorials = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum_of_factorials += factorial(digit)
    temp //= 10
if sum_of_factorials == n:
    print(f"{n} is a Strong Number")
else:
    print(f"{n} is not a Strong Number")