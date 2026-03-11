operator = input("Enter your operator (+ - * /): ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")