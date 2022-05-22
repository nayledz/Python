from collections import deque

cups_capacity = deque([int(x) for x in input().split()])
bottles_capacity = deque([int(x) for x in input().split()])

wasted_liters = 0

while bottles_capacity:
    if cups_capacity:
        current_cup = cups_capacity[0]
        current_bottle = bottles_capacity[-1]

        if current_bottle >= current_cup:
            cups_capacity.popleft()
            wasted_liters += current_bottle - current_cup
            bottles_capacity.pop()
        else:
            cups_capacity[0] -= current_bottle
            bottles_capacity.pop()
            if cups_capacity[0] <= 0:
                break
    else:
        break

bottles_capacity = [str(x) for x in bottles_capacity]
cups_capacity = [str(x) for x in cups_capacity]

if not cups_capacity:
    print(f"Bottles: {' '.join(bottles_capacity)}")
else:
    print(f"Cups: {' '.join(cups_capacity)}")

print(f"Wasted litters of water: {wasted_liters}")