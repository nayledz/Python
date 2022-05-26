size = int(input())

matrix = []
for _ in range(size):
    nums = [int(x) for x in input().split()]
    matrix.append(nums)

primary_diagonal = []
secondary_diagonal = []

for index in range(size):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][size - 1 - index])

sums_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))
print(sums_difference)