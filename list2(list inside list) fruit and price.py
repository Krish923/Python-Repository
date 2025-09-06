fruit_count = int(input())
fruit_prices = []

for i in range(fruit_count):
    name = input()
    price = int(input())
    fruit_data = [name, price]
    fruit_prices.append(fruit_data)

first_fruit = fruit_prices[0]
print("First fruit:", first_fruit[0])

cheap_fruits = []
for fruit in fruit_prices:
    if fruit[1] < 10:
        cheap_fruits.append(fruit)
print("Cheap count:", len(cheap_fruits))
