unit = input("Please enter your unit: ")
temp = float(input("Please enter your temperature: "))

if unit == "C":
    print("Your temperature is", temp*33.8, "fahrenheit")
elif unit == "F":
    print("Your temperature is", temp/33.8, "celsius ")