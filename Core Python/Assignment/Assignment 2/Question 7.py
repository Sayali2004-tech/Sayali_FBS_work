
num = int(input("Enter a three-digit number: "))

hundreds = num // 100
tens = (num % 100) // 10
ones = num % 10

sum_of_digits = hundreds + tens + ones

print("Sum of digits:", sum_of_digits)
