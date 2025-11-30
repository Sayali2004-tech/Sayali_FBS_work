#Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. Based on this calculate the total salary of each emp and also total salary of all emp.
n = int(input("Enter number of employees: "))
total_all_employees = 0

for i in range(1, n + 1):
    basic = float(input(f"Enter basic salary of employee {i}: "))
    
    if basic < 20000:
        da = 0.10 * basic
        ta = 0.12 * basic
        hra = 0.15 * basic
    else:
        da = 0.15 * basic
        ta = 0.18 * basic
        hra = 0.20 * basic

    total_salary = basic + da + ta + hra
    total_all_employees += total_salary

    print(f"Total salary of employee {i}: {total_salary:.2f}")

print(f"Total salary of all employees: {total_all_employees:.2f}")
