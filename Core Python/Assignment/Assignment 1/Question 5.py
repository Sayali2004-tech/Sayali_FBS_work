
P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))

CI = P * (1 + R / 100) ** T - P


print("Compound Interest =", CI)
