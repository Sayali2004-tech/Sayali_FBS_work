#Write a program to check if entered number is a palindrome or not.
def is_palindrome(num):
    original = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev == original

number = int(input("Enter a number: "))

if is_palindrome(number):
    print(number, "is a palindrome")
else:
    print(number, "is not a palindrome")
