def get_children(row, col, size):
    possible_children = [
        [row - 1, col],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col]
    ]

    result = []
    for child_row, child_col in possible_children:
        if not is_outside(child_row, child_col, size):
            result.append([child_row, child_col])
    return result


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def next_pos(row, col, command):
    if command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1
    elif command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col


number_of_presents = int(input())
neighborhood_size = int(input())

matrix = []
santa_row = 0
santa_col = 0
nice_kids = 0

for row in range(neighborhood_size):
    row_elements = input().split()
    for col in range(neighborhood_size):
        if row_elements[col] == "S":
            santa_row = row
            santa_col = col
        elif row_elements[col] == "V":
            nice_kids += 1
    matrix.append(row_elements)

happy_kids = 0
while number_of_presents:
    command = input()
    if command == 'Christmas morning':
        break
    direction = command
    next_row, next_col = next_pos(santa_row, santa_col, direction)
    if is_outside(next_row, next_col, neighborhood_size):
        continue

    if matrix[next_row][next_col] == "X":
        matrix[santa_row][santa_col] = "-"
        santa_row, santa_col = next_row, next_col
        matrix[next_row][next_col] = "S"

    elif matrix[next_row][next_col] == "V":
        number_of_presents -= 1
        nice_kids -= 1
        happy_kids += 1
        matrix[santa_row][santa_col] = "-"
        santa_row, santa_col = next_row, next_col
        matrix[next_row][next_col] = "S"

    elif matrix[next_row][next_col] == "C":
        matrix[next_row][next_col] = "S"
        children = get_children(next_row, next_col, neighborhood_size)
        for child_row, child_col in children:
            if matrix[child_row][child_col] != '-':
                number_of_presents -= 1
                if matrix[child_row][child_col] == "V":
                    happy_kids += 1
                    nice_kids -= 1
                matrix[child_row][child_col] = '-'

    if number_of_presents < 0:
        break
    matrix[santa_row][santa_col] = "-"
    santa_row, santa_col = next_row, next_col
    matrix[next_row][next_col] = "S"


if number_of_presents <= 0 < nice_kids:
    print("Santa ran out of presents!")

for row in matrix:
    print(' '.join(row))

if nice_kids == 0:
    print(f"Good job, Santa! {happy_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids} nice kid/s.")

