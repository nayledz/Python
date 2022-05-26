size = int(input())

matrix = []
for _ in range(size):
    nums = [int(x) for x in input().split(", ")]
    matrix.append(nums)

primary_diagonal = []
secondary_diagonal = []

for index in range(size):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][size - 1 - index])

print(f"Primary diagonal: {', '.join([str(x) for x in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")