number_of_orders = int(input())

price = 0
total_price = 0
for i in range(1, number_of_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())
    price = price_per_capsule * days * capsules_count
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")