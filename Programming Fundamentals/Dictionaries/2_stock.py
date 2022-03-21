data = input().split(" ")
searched_products = input().split(" ")

products = {}

for i in range(0, len(data), 2):
    key = data[i]
    values = data[i+1]
    products[key] = int(values)

for j in searched_products:
    if j in products:
        print(f"We have {products[j]} of {j} left")
    else:
        print(f"Sorry, we don't have {j}")

