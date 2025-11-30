#Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
n = int(input("Enter n: "))

def fact(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f

total = 0
for i in range(1, n+1):
    total += fact(i)

print("Sum =", total)


#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
N = int(input("Enter N: "))

total = 0
for i in range(1, N+1):
    total += N ** i

print("Sum =", total)

#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter n: "))

total = 0
term = 1

for i in range(n):
    total += term
    term *= 2

print("Sum =", total)

#d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
a = float(input("Enter a: "))

total = 0
for i in range(1, 11):
    total += (a ** i) / i

print("Sum =", total)

# e. x - x2/3 + x3/5 - x4/7 + .... to n terms
x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

total = 0
sign = 1
den = 1

for i in range(1, n+1):
    total += sign * (x ** i) / den
    sign *= -1      # alternate + and -
    den += 2        # denominator: 1, 3, 5, 7...

print("Sum =", total)
