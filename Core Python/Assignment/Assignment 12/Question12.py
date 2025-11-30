s = input("Enter a string: ")
count = sum(1 for c in s if 'a' <= c <= 'z')
print("Lowercase letters:", count)
