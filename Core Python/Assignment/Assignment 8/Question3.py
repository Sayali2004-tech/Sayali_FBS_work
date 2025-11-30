#Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

n = int(input("Enter n: "))
print("Sum =", sum_n(n))

#b. 1!+ 2! + 3! + 4!+..... + n!
def factorial(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f

def sum_factorials(n):
    total = 0
    for i in range(1, n+1):
        total += factorial(i)
    return total

n = int(input("Enter n: "))
print("Sum of factorial series =", sum_factorials(n))

#c. 1^1 + 2^2 + 3^3+ ...... n^n
def sum_power_series(n):
    total = 0
    for i in range(1, n+1):
        total += i ** i
    return total

n = int(input("Enter n: "))
print("Sum of power series =", sum_power_series(n))
