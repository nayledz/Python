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


string = input()
size = int(input())

matrix = []
for row in range(size):
    row_elements = input()
    matrix.append([ch for ch in row_elements])

player_row, player_col = 0, 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "P":
            player_row, player_col = row, col

number = int(input())

directions = []
for num in range(number):
    command = input()
    directions.append(command)

for direction in directions:
    next_row, next_col = get_next_pos(player_row, player_col, direction)

    if is_outside(next_row, next_col, size):
        string = string[:-1]
        continue

    if (matrix[next_row][next_col]).isalpha():
        string += (matrix[next_row][next_col])

    matrix[player_row][player_col] = "-"
    player_row, player_col = next_row, next_col
    matrix[player_row][player_col] = "P"

print(string)
for row in matrix:
    print(''.join(row))