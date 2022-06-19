from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])

gemstones = 0
porcelain_sculptures = 0
gold = 0
diamond_jewellery = 0

while materials and magic:
    current_material = materials.pop()
    current_magic = magic.popleft()
    sum = current_magic + current_material

    if sum < 100 and sum % 2 == 0:
        current_material = 2 * current_material
        current_magic = 3 * current_magic
        sum = current_material + current_magic

    elif sum < 100 and sum % 2 != 0:
        sum = 2 * sum

    elif sum > 499:
        sum= sum / 2

    if 100 <= sum <= 199:
        gemstones += 1
    elif 200 <= sum <= 299:
        porcelain_sculptures += 1
    elif 300 <= sum <= 399:
        gold += 1
    elif 400 <= sum <= 499:
        diamond_jewellery += 1

if (gemstones > 0 and porcelain_sculptures > 0) or (gold > 0 and diamond_jewellery > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    materials = [str(x) for x in materials]
    print(f"Materials left: {', '.join(materials)}")
if magic:
    magic = [str(x) for x in magic]
    print(f"Magic left: {', '.join(magic)}")

if diamond_jewellery > 0:
    print(f"Diamond Jewellery: {diamond_jewellery}")
if gemstones > 0:
    print(f"Gemstone: {gemstones}")
if gold > 0:
    print(f"Gold: {gold}")
if porcelain_sculptures > 0:
    print(f"Porcelain Sculpture: {porcelain_sculptures}")


