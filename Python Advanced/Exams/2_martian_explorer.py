def get_next_pos(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1

def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size

def next_pos(row, col, command):
    if command == "up":
        return 5, col
    elif command == "down":
        return 0, col
    elif command == "left":
        return row, 5
    elif command == "right":
        return row, 0

size = 6

one_rover_row = 0
one_rover_col = 0
matrix = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "E":
            one_rover_row = row
            one_rover_col = col
    matrix.append(row_elements)

commands = input().split(', ')

water_found = 0
metal_found = 0
concrete_found = 0


for command in commands:
    next_row, next_col = get_next_pos(one_rover_row, one_rover_col, command)
    if is_outside(next_row, next_col, size):
        next_row, next_col = next_pos(one_rover_row, one_rover_col, command)

    if matrix[next_row][next_col] == "W":
        water_found += 1
        print(f'Water deposit found at {next_row, next_col}')

    elif matrix[next_row][next_col] == "M":
        metal_found += 1
        print(f'Metal deposit found at {next_row, next_col}')

    elif matrix[next_row][next_col] == "C":
        concrete_found += 1
        print(f'Concrete deposit found at {next_row, next_col}')

    elif matrix[next_row][next_col] == "R":
        print(f"Rover got broken at ({next_row}, {next_col})")
        break

    matrix[one_rover_row][one_rover_col] = "-"
    one_rover_row, one_rover_col = next_row, next_col
    matrix[next_row][next_col] = "E"

if water_found and metal_found and concrete_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")

