weight = float(input("Enter your weight: "))
unit = input("Enter your unit: ")

if unit == "kg":
    print("Your weight is", weight*2.2, "lbs")
elif unit == "lb":
    print("Your weight is", weight/2.2, "lbs")