from collections import deque

fireworks_effects = deque([int(x) for x in input().split(', ')])
explosive_power = [int(x) for x in input().split(', ')]

palm_fireworks = 0
willow_fireworks = 0
crossette_firework = 0

while fireworks_effects and explosive_power:
    current_firework = fireworks_effects[0]
    current_power = explosive_power[-1]
    mix = current_firework + current_power

    if current_power <= 0:
        explosive_power.pop()
        continue
    if current_firework <= 0:
        fireworks_effects.popleft()
        continue

    if mix % 3 == 0 and mix % 5 != 0:
        palm_fireworks += 1
    elif mix % 3 != 0 and mix % 5 == 0:
        willow_fireworks += 1
    elif mix % 3 == 0 and mix % 5 == 0:
        crossette_firework += 1
    else:
        fireworks_effects[0] -= 1
        fireworks_effects.append(fireworks_effects[0])
        fireworks_effects.popleft()
        continue

    explosive_power.pop()
    fireworks_effects.popleft()

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_firework >= 3:
        break

if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    fireworks_effects = [str(el) for el in fireworks_effects]
    print(f"Firework Effects left: {', '.join(fireworks_effects)}")

if explosive_power:
    explosive_power = [str(el) for el in explosive_power]
    print(f" Explosive Power left: {', '.join(explosive_power)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_firework}")

