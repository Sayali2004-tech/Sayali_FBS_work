s = input("Enter a string: ")
n = int(input("Enter index to remove: "))
s = s[:n] + s[n+1:]
print("Modified string:", s)
