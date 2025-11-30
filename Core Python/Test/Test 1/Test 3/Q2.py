#Write a program to calculate the sum of following series where n is input by user.
#1/1! + 2/2! + 3/3! + 4/4! + ... N/N!

def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

n = int(input("Enter the value of n: "))
sum_series = 0

for i in range(1, n + 1):
    sum_series += i / factorial(i)

print("Sum of the series:", sum_series)
