def is_outside(row, col, rows, cols):
    return row < 0 or col < 0 or row >= rows or col >= cols


rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append(input().split())

while True:
    command = input()
    if command == "END":
        break
    command = command.split()
    if len(command) != 5 or command[0] != "swap":
        print('Invalid input!')
        continue
    row1, col1, row2, col2 = [int(x) for x in command[1:]]

    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print('Invalid input!')
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
    for row in matrix:
        print(*row, sep=' ')