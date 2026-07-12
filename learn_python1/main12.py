# Shopping Cart python program 

foods= []
prices=[]
total=0

while True:
    food= input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price=float(input(f"Enter the price of {food}:Rs "))
        foods.append(food)
        prices.append(price)

print("your Cart")
for food in foods:
    print(food)
for price in prices:
    total = total + price
print(f"your total is :Rs{total:.2f}")

