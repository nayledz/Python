def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


rows = int(input())

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

input_line = input()

while input_line != 'END':
    command, row, col, value = input_line.split()
    row = int(row)
    col = int(col)
    if is_outside(row, col, rows):
        print("Invalid coordinates")
    else:
        if command == "Add":
            matrix[row][col] += int(value)
        elif command == "Subtract":
            matrix[row][col] -= int(value)
    input_line = input()

for row in matrix:
    row = [str(x) for x in row]
    print(' '.join(row))