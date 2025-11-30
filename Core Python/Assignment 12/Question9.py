s = input("Enter a string: ")
words = len(s.split())
chars = sum(1 for c in s if c != ' ')
print("Words:", words, "Characters (excluding spaces):", chars)
