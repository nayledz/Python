def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size

size = 6
matrix = []
positions = []

for _ in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

total_sum = 0

for _ in range(3):
    input_line = input()
    position = ''
    for ch in input_line:
        if ch != "(" and ch != ")":
            position += ch
    row, col = [int(x) for x in position.split(', ')]
    if [row, col] in positions:
        continue
    positions.append([row, col])

    if is_outside(row, col, size):
        continue

    if matrix[row][col] == "B":
        for current_row in range(size):
            if matrix[current_row][col] != "B":
                total_sum += int(matrix[current_row][col])

if 100 <= total_sum <= 199:
    print(f"Good job! You scored {total_sum} points, and you've won Football.")
elif 200 <= total_sum <= 299:
    print(f"Good job! You scored {total_sum} points, and you've won Teddy Bear.")
elif 300 <= total_sum:
    print(f"Good job! You scored {total_sum} points, and you've won Lego Construction Set.")
else:
    print(f"Sorry! You need {100 - total_sum} points more to win a prize.")

