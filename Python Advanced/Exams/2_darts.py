def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = 7
matrix = []

first_player, second_player = input().split(', ')

for _ in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

first_player_points = 501
second_player_points = 501


index = 0
first_index = 0
second_index = 0

while True:
    row, col = tuple(map(int, input().replace('(', '').replace(')', '').split(', ')))

    index += 1

    if is_outside(row, col, size):
        if index % 2 != 0:
            first_index += 1
        else:
            second_index += 1
        continue

    if matrix[row][col].isnumeric():
        if index % 2 != 0:
            first_index += 1
            first_player_points -= int(matrix[row][col])
        else:
            second_index += 1
            second_player -= int(matrix[row][col])

    elif matrix[row][col] == "D":
        sum = 2 * (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(matrix[row][6]))
        if index % 2 != 0:
            first_index += 1
            first_player_points -= sum
        else:
            second_index += 1
            second_player_points -= sum

    elif matrix[row][col] == "T":
        sum = 3 * (int(matrix[0][col]) + int(matrix[6][col]) + int(matrix[row][0]) + int(
            matrix[row][6]))
        if index % 2 != 0:
            first_index += 1
            first_player_points -= sum
        else:
            second_index += 1
            second_player_points -= sum

    elif matrix[row][col] == "B":
        if index % 2 != 0:
            first_index += 1
            print(f"{first_player} won the game with {first_index} throws!")
            break
        else:
            second_index += 1
            print(f"{second_player} won the game with {second_index} throws!")
            break
    if first_player_points <= 0 or second_player_points <= 0:
        break


if first_player_points <= 0:
    print(f"{first_player} won the game with {first_index} throws!")
elif second_player_points <= 0:
    print(f"{second_player} won the game with {second_index} throws!")
