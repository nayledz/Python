rows, cols = [int(x) for x in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

square_matrices = 0
for row_index in range(rows - 1):
    for col_index in range(cols - 1):
        if matrix[row_index][col_index] ==\
                matrix[row_index + 1][col_index] ==\
                matrix[row_index][col_index + 1] ==\
                matrix[row_index + 1][col_index + 1]:
            square_matrices += 1
print(square_matrices)