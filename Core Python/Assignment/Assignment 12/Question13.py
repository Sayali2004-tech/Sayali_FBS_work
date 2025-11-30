s = input("Enter a string: ")
digits = sum(1 for c in s if c.isdigit())
letters = sum(1 for c in s if c.isalpha())
print("Letters:", letters, "Digits:", digits)
