foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy(q to quit): ")
    if food.lower() == "q":
        break
    price = float(input(f"Enter a price of a {food}: "))
    foods.append(food)
    prices.append(price)

print("-----YOUR CART-----")
for food in foods:
    print(food)

total = sum(prices)
print(f"your total is: {total}")