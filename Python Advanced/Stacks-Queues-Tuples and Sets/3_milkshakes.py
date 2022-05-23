from collections import deque
chocolates = [int(x) for x in input().split(', ')]
cups_of_milk = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while chocolates and cups_of_milk:
    current_chocolate = chocolates[-1]
    current_cup = cups_of_milk[0]

    if milkshakes == 5:
        break
        
    if current_cup <= 0 and current_chocolate <= 0:
        cups_of_milk.popleft()
        chocolates.pop()
        continue

    if current_cup <= 0:
        cups_of_milk.popleft()
        continue

    if current_chocolate <= 0:
        chocolates.pop()
        continue

    if current_chocolate == current_cup:
        chocolates.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        cups_of_milk.append(cups_of_milk.popleft())
        chocolates[-1] -= 5


if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    chocolates = [str(x) for x in chocolates]
    print(f"Chocolate: {', '.join(chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    cups_of_milk = [str(x) for x in cups_of_milk]
    print(f"Milk: {', '.join(cups_of_milk)}")
else:
    print("Milk: empty")