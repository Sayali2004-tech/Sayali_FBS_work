s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
length1 = length2 = 0
for _ in s1: length1 += 1
for _ in s2: length2 += 1
print("Larger string:", s1 if length1 > length2 else s2)
