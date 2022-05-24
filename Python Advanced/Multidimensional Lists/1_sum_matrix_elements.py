rows, cols = [int(el) for el in input().split(', ')]
matrix = []
result = 0

for _ in range(rows):
    nums = [int(el) for el in input().split(', ')]
    result += sum(nums)
    matrix.append(nums)

print(result)
print(matrix)