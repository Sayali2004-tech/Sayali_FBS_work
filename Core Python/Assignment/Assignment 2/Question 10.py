
num = int(input("Enter a three-digit number: "))

hundreds = num // 100
tens = (num % 100) // 10
ones = num % 10

reversed_num = ones * 100 + tens * 10 + hundreds

print("Reversed number:", reversed_num)
