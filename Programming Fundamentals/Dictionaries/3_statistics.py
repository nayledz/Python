command = input()
products = {}

while command != "statistics":
    data = command.split(": ")
    product = data[0]
    quantity = int(data[1])

    if product in products:
        products[product] += quantity
    else:
        products[product] = quantity

    command = input()

print("Products in stock:")
for product, quantity in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")