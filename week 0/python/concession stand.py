menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("------------------------")
while True:
    choice = input("Choose a menu option(q for quit): ").lower()
    if choice == "q":
        break
    if menu.get(choice):
        cart.append(choice)

print("--------- CART ---------")
total = 0
for item in cart:
    total += menu.get(item)
    print(f"{item:10}: ${menu.get(item):.2f}")
print("------------------------")

print("--------- TOTAL ---------")
print(f"total is: ${total:.2f}")
print("------------------------")