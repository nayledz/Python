from collections import deque

elf_energies = deque([int(x) for x in input().split()])
number_of_materials = [int(x) for x in input().split()]

total_energy = 0
total_number_of_toys = 0
turn = 0

while elf_energies and number_of_materials:
    while elf_energies and elf_energies[0] < 5:
        elf_energies.popleft()

    if not elf_energies:
        break

    current_elf_energy = elf_energies.popleft()
    current_box = number_of_materials.pop()
    turn += 1

    toys_to_be_created_count = 1
    energy_to_be_spent = current_box
    energy_increase_factoy = 1

    if turn % 3 == 0:
        toys_to_be_created_count = 2
        energy_to_be_spent *= 2
    if turn % 5 == 0:
        toys_to_be_created_count = 0
        energy_increase_factoy = 0

    if energy_to_be_spent <= current_elf_energy:
        total_number_of_toys += toys_to_be_created_count
        total_energy += energy_to_be_spent
        elf_energies.append(current_elf_energy - energy_to_be_spent + energy_increase_factoy)
    else:
        number_of_materials.append(current_box)
        elf_energies.append(current_elf_energy * 2)




print(f"Toys: {total_number_of_toys}")
print(f"Energy: {total_energy}")
if elf_energies:
    elf_energies = [str(x) for x in elf_energies]
    print(f"Elves left: {', '.join(elf_energies)}")
if number_of_materials:
    number_of_materials = [str(x) for x in number_of_materials]
    print(f"Boxes left: {', '.join(number_of_materials)}")





