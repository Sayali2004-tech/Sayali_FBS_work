P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest (%): "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100

print("50 Simple Interest =", round(SI, 2))
print("Total Amount =", round(P + SI, 2))