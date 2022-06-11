strings = input().split("|")

matrix = []

for idx in range(len(strings) - 1, -1, -1):
    matrix.extend(strings[idx].strip().split())

print(' '.join(matrix))
