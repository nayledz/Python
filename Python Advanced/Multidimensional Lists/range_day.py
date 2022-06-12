def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def next_pos(row, col, command, steps):
    if command == "left":
        return row, col - steps
    elif command == "right":
        return row, col + steps
    elif command == "up":
        return row - steps, col
    elif command == "down":
        return row + steps, col

size = 5
matrix = []
position_row = 0
position_col = 0
targets = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "A":
            position_row = row
            position_col = col
        elif row_elements[col] == "x":
            targets += 1
    matrix.append(row_elements)

number_of_commands = int(input())

matrix[position_row][position_col] = '.'
targets_idx = []

for _ in range(number_of_commands):
    command = input().split()
    direction = command[1]

    if command[0] == "move":
        steps = int(command[2])

        next_row, next_col = next_pos(position_row, position_col, direction, steps)

        if not is_outside(next_row, next_col, size) and matrix[next_row][next_col] == ".":
            position_row, position_col = next_row, next_col

    elif command[0] == "shoot":

        next_row, next_col = next_pos(position_row, position_col, direction, 1)
        while not is_outside(next_row, next_col, size):
            if matrix[next_row][next_col] == 'x':
                targets -= 1
                matrix[next_row][next_col] = "."
                targets_idx.append([next_row, next_col])
                break
            next_row, next_col = next_pos(next_row, next_col, direction, 1)
        if targets == 0:
            break

if targets == 0:
    print(f"Training completed! All {len(targets_idx)} targets hit.")
else:
    print(f"Training not completed! {targets} targets left.")


print(*targets_idx, sep='\n')
