#Write a program find reverse of a number
def reverse_number(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev

number = int(input("Enter a number: "))
print("Reversed number =", reverse_number(number))
