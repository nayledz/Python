def get_next_pos(row, col, command):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1

def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols

def next_pos(row, col, rows, cols, command):
    if command == "up":
        return rows - 1, col
    elif command == "down":
        return 0, col
    elif command == "left":
        return row, cols - 1
    elif command == "right":
        return row, 0


rows, columns = [int(x) for x in input().split(', ')]


matrix = []
santa_row, santa_col = 0, 0
decorations = 0
gifts = 0
cookies = 0

for row in range(rows):
    row_elements = input().split()
    for col in range(columns):
        if row_elements[col] == "Y":
            santa_row, santa_col = row, col
        elif row_elements[col] == "D":
            decorations += 1
        elif row_elements[col] == "G":
            gifts += 1
        elif row_elements[col] == "C":
            cookies += 1
    matrix.append(row_elements)

collected_decorations = 0
collected_gifts = 0
collected_cookies = 0
collected_all = False

input_line = input()
while input_line != "End":
    command = input_line.split('-')
    direction = command[0]
    steps = int(command[1])

    for _ in range(1, steps + 1):
        next_row, next_col = get_next_pos(santa_row, santa_col, direction)
        if is_outside(next_row, next_col, rows, columns):
            next_row, next_col = next_pos(next_row, next_col, rows, columns, direction)
        if matrix[next_row][next_col] == "D":
            collected_decorations += 1
            decorations -= 1
        elif matrix[next_row][next_col] == "G":
            collected_gifts += 1
            gifts -= 1
        elif matrix[next_row][next_col] == "C":
            collected_cookies += 1
            cookies -= 1

        matrix[santa_row][santa_col] = "x"
        santa_row, santa_col = next_row, next_col
        matrix[santa_row][santa_col] = "Y"

        if decorations == 0 and gifts == 0 and cookies == 0:
            collected_all = True
            break
    if collected_all:
        break
    input_line = input()


if decorations == 0 and gifts == 0 and cookies == 0:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {collected_decorations} Christmas decorations")
print(f"- {collected_gifts} Gifts")
print(f"- {collected_cookies} Cookies")
for row in matrix:
    print(' '.join(row))
