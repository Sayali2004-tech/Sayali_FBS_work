#Write a program to check if entered year is a leap year or not.
def is_leap_year(year):
    # Leap year if divisible by 4 and (not divisible by 100 unless divisible by 400)
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
