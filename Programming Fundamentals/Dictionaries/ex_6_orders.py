products_dict = {}
while True:
    command = input()
    if command == "buy":
        break
    else:
        command = command.split(" ")
        item = command[0]
        price = float(command[1])
        quantity = int(command[2])
        if item not in products_dict:
            products_dict[item] = [price, quantity]
        else:
            products_dict[item] = [price, (products_dict[item][1] + quantity)]

for key, value in products_dict.items():
    print(f"{key} -> {(value[0] * value[1]):.2f}")
