
# Lab 10
# Mina

# Reflection 1
# I didn't know you could use negative numbers to get items
# from the end of a list. I also thought changing a list
# would be harder, but Python makes it pretty simple.

# Reflection 2
# When I worked at a hotel, we had to keep track of supplies
# for activities and events. Using a list would have made it
# easier to keep track of everything instead of entering
# everything manually into Excel.


# Exercise 1

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# Exercise 2

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed, which is useful for coordinates because the values stay the same.")

print(coords)


# Exercise 6

sales = [100, 250, 75, 480, 200]

print("Total:", sum(sales))
print("Count:", len(sales))
print("Average:", sum(sales) / len(sales))
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    new_price = round(price * 0.9, 2)
    discounted.append(new_price)

print("Original:", prices)
print("Discounted:", discounted)


# Exercise 8

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
