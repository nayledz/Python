from collections import deque
working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
making_process = deque(input().split())

honey = 0

while working_bees and nectar:
    current_bee = working_bees.popleft()
    current_nectar = nectar.pop()
    if current_nectar >= current_bee:
        current_symbol = making_process.popleft()
        if current_symbol == "/":
            if current_nectar > 0:
                honey += abs(current_bee / current_nectar)
        elif current_symbol == "+":
            honey += abs(current_bee + current_nectar)
        elif current_symbol == "-":
            honey += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            honey += abs(current_bee * current_nectar)
    else:
        working_bees.appendleft(current_bee)

print(f"Total honey made: {honey}")
if working_bees:
    working_bees = [str(x) for x in working_bees]
    print(f"Bees left: {', '.join(working_bees)}")
if nectar:
    nectar = [str(x) for x in nectar]
    print(f"Nectar left: {', '.join(nectar)}")