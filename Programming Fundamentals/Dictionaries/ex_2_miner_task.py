my_dict = {}

while True:
    resource = input()
    if resource == "stop":
        break
    else:
        quantity = int(input())
        if resource in my_dict:
            my_dict[resource] += quantity
        else:
            my_dict[resource] = quantity

for (resource, quantity) in my_dict.items():
    print(f"{resource} -> {quantity}")
