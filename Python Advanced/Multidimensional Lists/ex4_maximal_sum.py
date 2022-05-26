rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

max_sum = 0
best_row = 0
best_col = 0
for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_sum = matrix[row_index][col_index] + matrix[row_index][col_index + 1] +\
                      matrix[row_index][col_index + 2] + matrix[row_index + 1][col_index] +\
                      matrix[row_index + 1][col_index + 1] + matrix[row_index + 1][col_index + 2] +\
                      matrix[row_index + 2][col_index] + matrix[row_index + 2][col_index + 1] +\
                      matrix[row_index + 2][col_index + 2]
        if current_sum >= max_sum:
            max_sum = current_sum
            best_col = col_index
            best_row = row_index

print(f"Sum = {max_sum}")
print(f"{matrix[best_row][best_col]} {matrix[best_row][best_col + 1]} {matrix[best_row][best_col + 2]}")
print(f"{matrix[best_row + 1][best_col]} {matrix[best_row + 1][best_col + 1]} {matrix[best_row + 1][best_col + 2]}")
print(f"{matrix[best_row + 2][best_col]} {matrix[best_row + 2][best_col + 1]} {matrix[best_row + 2][best_col + 2]}")