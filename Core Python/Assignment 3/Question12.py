num = int(input("Enter a 3-digit number: "))
if 100 <= num <= 999:
    num_str = str(num) 
    if num_str[0] == num_str[2]:
        print(num, "is a Palindrome number.")
    else:
        print(num, "is NOT a Palindrome number.")
else:
    print("Please enter a valid 3-digit number.")