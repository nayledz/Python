from collections import deque
materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

presents = {
    150: ["Doll", 0],
    250: ["Wooden train", 0],
    300: ["Teddy bear", 0],
    400: ["Bicycle", 0]
}

while materials and magic_level:
    current_material = materials[-1]
    current_magic = magic_level[0]

    if current_magic == 0 and current_material == 0:
        magic_level.popleft()
        materials.pop()
        continue

    if current_magic == 0:
        magic_level.popleft()
        continue

    if current_material == 0:
        materials.pop()
        continue

    total_magic = current_magic * current_material
    if total_magic in presents:
        presents[total_magic][1] += 1
        materials.pop()
        magic_level.popleft()
    else:

        if total_magic < 0:
            total_magic = current_material + current_magic
            materials.pop()
            magic_level.popleft()
            materials.append(total_magic)
        elif total_magic > 0:
            magic_level.popleft()
            materials[-1] += 15

crafted_presents = False
if presents[150][1] > 0 and presents[250][1] > 0:
    crafted_presents = True

if presents[300][1] > 0 and presents[400][1] > 0:
    crafted_presents = True

if crafted_presents:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

materials = [str(x) for x in materials]

if len(materials) > 0:
    print(f"Materials left: {', '.join(reversed(materials))}")

magic_level = [str(x) for x in magic_level]
if magic_level:
    print(f"Magic left: {', '.join(magic_level)}")

for present, count in sorted(presents.values()):
    if count > 0:
        print(f"{''.join([present])}: {count}")



