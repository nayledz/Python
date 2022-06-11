def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def get_next_pos(row, col, command):
    if command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1
    elif command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col


size_field = int(input())
commands = input().split()

coals = set()
miner_row = 0
miner_col = 0


matrix = []

for row in range(size_field):
    row_elements = list(input().split())
    for col in range(size_field):
        if row_elements[col] == 's':
            miner_row = row
            miner_col = col
        elif row_elements[col] == 'c':
            coals.add(f'{row} {col}')
    matrix.append(row_elements)

dead = False

for command in commands:

    next_row, next_col = get_next_pos(miner_row, miner_col, command)
    matrix[miner_row][miner_col] = "*"

    if is_outside(next_row, next_col, size_field):
        continue
    elif matrix[next_row][next_col] == "e":
        miner_row, miner_col = next_row, next_col
        dead = True
        print(f"Game over! ({miner_row}, {miner_col})")
        break
    elif matrix[next_row][next_col] == "c":
        miner_row, miner_col = next_row, next_col
        matrix[next_row][next_col] = "s"
    else:
        matrix[next_row][next_col] = 's'
        miner_row, miner_col = next_row, next_col

number_of_remaining_coal = 0
coals_missing = True

for row in range(size_field):
    for col in range(size_field):
        if matrix[row][col] == 'c':
            coals_missing = False
            number_of_remaining_coal += 1

if number_of_remaining_coal == 0 and not dead:
    print(f"You collected all coal! ({miner_row}, {miner_col})")
elif not coals_missing and not dead:
    print(f"{number_of_remaining_coal} pieces of coal left. ({miner_row}, {miner_col})")