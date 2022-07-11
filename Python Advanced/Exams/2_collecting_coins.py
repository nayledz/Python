import math


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def get_next_pos(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


def next_pos(row, col, size, command):
    if command == "up":
        return size - 1, col
    elif command == "down":
        return 0, col
    elif command == "left":
        return row, size - 1
    elif command == "right":
        return row, 0


size = int(input())

matrix = []
player_row, player_col = 0, 0


for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "P":
            player_row, player_col = row, col
    matrix.append(row_elements)

won = False
lost = False
coins = 0
path = [[player_row, player_col]]

while True:
    direction = input()
    if direction not in ['up', 'down', 'left', 'right']:
        continue

    next_row, next_col = get_next_pos(player_row, player_col, direction)
    if is_outside(next_row, next_col, size):
        next_row, next_col = next_pos(player_row, player_col, size, direction)

    if (matrix[next_row][next_col]).isdigit() and [next_row, next_col] not in path:
        coins += int(matrix[next_row][next_col])

    elif matrix[next_row][next_col] == "X":
        coins -= 0.5 * coins
        lost = True
        path.append([next_row, next_col])
        break

    if coins >= 100:
        won = True
        path.append([next_row, next_col])
        break

    player_row, player_col = next_row, next_col
    path.append([next_row, next_col])


if lost:
    print(f"Game over! You've collected {math.floor(coins)} coins.")
if won:
    print(f"You won! You've collected {math.floor(coins)} coins.")

print('Your path:')
for el in path:
    print(el)




