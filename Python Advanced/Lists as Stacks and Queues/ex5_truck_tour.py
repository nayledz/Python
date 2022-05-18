from collections import deque

petrol_pumps = int(input())
pumps = deque()

for pump in range(petrol_pumps):
    pumps.append([int(x) for x in input().split()])

for attempt in range(petrol_pumps):
    tank = 0
    is_failed = False
    for petrol, distance in pumps:
        tank = tank + petrol - distance
        if tank < 0:
            is_failed = True
            break
    if is_failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break