gender = input("Enter gender (male/female): ").strip().lower()
age = int(input("Enter age: "))
if gender == "male":
    if age >= 21:
        print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")
elif gender == "female":
    if age >= 18:
        print("Eligible for marriage.")
    else:
        print("Not eligible for marriage.")
else:
    print("Invalid gender entered.")