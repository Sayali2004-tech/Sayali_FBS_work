#Write a program to find print the following Fibonacci series using functions:
#1 1 2 3 5 8 n terms
def fibonacci(n):
    a, b = 1, 1
    print(a, b, end=" ")

    for i in range(3, n+1):
        c = a + b
        print(c, end=" ")
        a, b = b, c

# main program
n = int(input("Enter number of terms: "))

if n == 1:
    print(1)
else:
    fibonacci(n)
