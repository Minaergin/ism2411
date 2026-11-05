
# Self Assessment

# QUestion 1
# The first bug I noticed was in the for loop because of the 
# missing colon after. And then the sales weren't being added 
# together but the syntax error helped me and I learned I need
# to pay more attention. 

# Question 2
# It takes the customers membership level and the original 
# price and applies the right discount based on their membership\
# such as bronze, gold or silver or the price stays the same 
# and it shows the final price. A colleague could use this just 
# by looking at the outputs.

# 3. I used ChatGPT to help me understand how the
# functions work and how to put the code together.


# Exercise 1

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        discount = 0.15
    elif tier == "silver":
        discount = 0.10
    elif tier == "bronze":
        discount = 0.05
    else:
        discount = 0

    new_price = price - (price * discount)
    return new_price

print(f"gold: ${apply_discount(200, 'gold'):.2f}")
print(f"silver: ${apply_discount(200, 'silver'):.2f}")
print(f"bronze: ${apply_discount(200, 'bronze'):.2f}")
print(f"none: ${apply_discount(200, 'none'):.2f}")


# Exercise 3

price = 200

discounted_price = apply_discount(price, "gold")
print(f"After gold discount: ${discounted_price:.2f}")

tax = calculate_tax(discounted_price, 0.07)
total = discounted_price + tax

print(f"After tax: ${total:.2f}")

def final_price(price, tier, tax_rate):
    new_price = apply_discount(price, tier)
    tax = calculate_tax(new_price, tax_rate)
    total = new_price + tax
    return total

answer = final_price(200, "gold", 0.07)
print(f'final_price(200, "gold", 0.07) = ${answer:.2f}')


# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")



# Exercise 5

sales = [120, 80, 250, 175, 90]

# Changed = to += so it adds all the sales together
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

# Added the missing colon
count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

# Changed <= to < so the index doesn't go past the list
i = 0
while i < len(sales):
    print(sales[i])
    i += 1



# Exercise 6

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# The x inside and outside of the function are different from each other.
# Original x stays the same when the inside function x is changed.
# which is why it prints 100, 1998, and 100
