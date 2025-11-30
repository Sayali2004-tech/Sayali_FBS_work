def armstrong_sum(num, power):
    if num == 0:
        return 0
    digit = num % 10
    return (digit ** power) + armstrong_sum(num // 10, power)
def is_armstrong(num):
    power = len(str(num))  
    return num == armstrong_sum(num, power)
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")